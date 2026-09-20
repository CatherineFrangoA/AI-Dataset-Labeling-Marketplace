from fastapi import APIRouter
from database import SessionLocal
from models.label_task import LabelTask

router = APIRouter(prefix="/api/task", tags=["Task"])


@router.post("/assign")
def assign_task(dataset_id: int, labeler_id: int):

    db = SessionLocal()

    task = LabelTask(
        dataset_id=dataset_id,
        labeler_id=labeler_id,
        status="assigned"
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()

    return {
        "message": "Task assigned successfully",
        "task_id": task.id,
        "dataset_id": task.dataset_id,
        "labeler_id": task.labeler_id,
        "status": task.status
    }
@router.put("/complete/{task_id}")
def complete_task(task_id: int):

    db = SessionLocal()

    task = db.query(LabelTask).filter(
        LabelTask.id == task_id
    ).first()

    if task is None:
        db.close()
        return {"message": "Task not found"}

    task.status = "completed"

    db.commit()
    db.refresh(task)
    db.close()

    return {
        "message": "Task completed successfully",
        "task_id": task.id,
        "status": task.status
    }