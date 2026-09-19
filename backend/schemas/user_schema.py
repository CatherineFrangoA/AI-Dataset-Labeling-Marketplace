from pydantic import BaseModel


class UserCreate(BaseModel):
    fullname: str
    email: str
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str