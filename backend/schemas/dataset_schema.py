from pydantic import BaseModel

class DatasetCreate(BaseModel):
    name: str
    filename: str
    owner_id: int