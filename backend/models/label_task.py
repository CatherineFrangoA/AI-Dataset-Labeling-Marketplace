from sqlalchemy import Column, Integer, String
from database import Base
class LabelTask(Base):
    __tablename__ = "label_tasks"
    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer)
    labeler_id = Column(Integer)
    status = Column(String, default="assigned")
