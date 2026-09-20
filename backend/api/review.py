from fastapi import APIRouter
from database import SessionLocal
from models.review import Review

router = APIRouter(prefix="/api/review", tags=["Review"])


@router.post("/submit")
def submit_review(task_id: int, reviewer_id: int, status: str):

    db = SessionLocal()

    review = Review(
        task_id=task_id,
        reviewer_id=reviewer_id,
        status=status
    )

    db.add(review)
    db.commit()
    db.refresh(review)
    db.close()

    return {
        "message": "Review submitted successfully",
        "review_id": review.id,
        "task_id": review.task_id,
        "reviewer_id": review.reviewer_id,
        "status": review.status
    }