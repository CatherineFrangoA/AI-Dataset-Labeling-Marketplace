from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from models.label_task import LabelTask
from core.auth import require_role

router = APIRouter(prefix="/api/task", tags=["Task"])


@router.post("/assign")
def assign_task(
    dataset_id: int,
    labeler_id: int,
    current_user: dict = Depends(require_role("admin"))
):
    db = SessionLocal()

    try:
        task = LabelTask(
            dataset_id=dataset_id,
            labeler_id=labeler_id,
            status="assigned"
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return {
            "message": "Task assigned successfully",
            "task_id": task.id,
            "dataset_id": task.dataset_id,
            "labeler_id": task.labeler_id,
            "status": task.status
        }
    finally:
        db.close()


@router.put("/complete/{task_id}")
def complete_task(
    task_id: int,
    current_user: dict = Depends(require_role("labeler"))
):
    db = SessionLocal()

    try:
        task = db.query(LabelTask).filter(
            LabelTask.id == task_id
        ).first()

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        if task.labeler_id != current_user["id"]:
            raise HTTPException(
                status_code=403,
                detail="You can complete only your assigned tasks"
            )

        task.status = "completed"
        db.commit()
        db.refresh(task)

        return {
            "message": "Task completed successfully",
            "task_id": task.id,
            "status": task.status
        }
    finally:
        db.close()