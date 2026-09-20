from sqlalchemy import Column, Integer, String
from database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer)
    reviewer_id = Column(Integer)
    status = Column(String, default="pending")