from fastapi.responses import FileResponse
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from database import SessionLocal
from models.dataset import Dataset
import os

router = APIRouter(prefix="/api/dataset", tags=["Dataset"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
def upload_dataset(
    name: str = Form(...),
    owner_id: int = Form(...),
    file: UploadFile = File(...)
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )

    filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        db = SessionLocal()

        try:
            dataset = Dataset(
                name=name,
                filename=filename,
                owner_id=owner_id,
                status="uploaded"
            )

            db.add(dataset)
            db.commit()
            db.refresh(dataset)

            return {
                "message": "Dataset uploaded successfully",
                "dataset_id": dataset.id,
                "filename": dataset.filename,
                "status": dataset.status
            }

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Dataset upload failed: {str(error)}"
        )


@router.get("/download/{dataset_id}")
def download_dataset(dataset_id: int):
    db = SessionLocal()

    try:
        all_datasets = db.query(Dataset).all()

        print(
            "DATABASE DATASETS:",
            [
                {
                    "id": item.id,
                    "filename": item.filename
                }
                for item in all_datasets
            ]
        )

        dataset = db.query(Dataset).filter(
            Dataset.id == dataset_id
        ).first()

        if dataset is None:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found in database"
            )

        file_path = os.path.join(
            UPLOAD_FOLDER,
            os.path.basename(dataset.filename)
        )

        print("DOWNLOAD FILE PATH:", file_path)

        if not os.path.isfile(file_path):
            raise HTTPException(
                status_code=404,
                detail="Dataset record found, but file is missing"
            )

        return FileResponse(
            path=file_path,
            filename=dataset.filename,
            media_type="text/csv"
        )

    finally:
        db.close()