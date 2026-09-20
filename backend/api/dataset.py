from fastapi.responses import FileResponse
from fastapi import APIRouter, UploadFile, File, Form
from database import SessionLocal
from models.dataset import Dataset
import os

router = APIRouter(prefix="/api/dataset", tags=["Dataset"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
def upload_dataset(
    name: str = Form(...),
    owner_id: int = Form(...),
    file: UploadFile = File(...)
):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    db = SessionLocal()

    dataset = Dataset(
        name=name,
        filename=file.filename,
        owner_id=owner_id,
        status="uploaded"
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    db.close()

    return {
        "message": "Dataset uploaded successfully",
        "dataset_id": dataset.id,
        "filename": dataset.filename,
        "status": dataset.status
    }
@router.get("/download/{dataset_id}")
def download_dataset(dataset_id: int):

    db = SessionLocal()

    dataset = db.query(Dataset).filter(
        Dataset.id == dataset_id
    ).first()

    db.close()

    if dataset is None:
        return {"message": "Dataset not found"}

    file_path = os.path.join(UPLOAD_FOLDER, dataset.filename)

    if not os.path.exists(file_path):
        return {"message": "Dataset file not found"}

    return FileResponse(
        path=file_path,
        filename=dataset.filename,
        media_type="text/csv"
    )