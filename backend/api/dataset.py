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