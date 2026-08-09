from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from agent import run_agent

app = FastAPI(title="AI Dataset Labeling Marketplace")

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String)


Base.metadata.create_all(bind=engine)


class UserCreate(BaseModel):
    fullname: str
    email: str
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class AgentRequest(BaseModel):
    data: list


@app.get("/")
def home():
    return "AI Dataset Labeling Marketplace"


@app.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        fullname=user.fullname,
        email=user.email,
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {
        "message": "Registration successful",
        "username": user.username
    }


@app.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if existing_user.password != user.password:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    db.close()

    return {
        "message": "Login successful",
        "username": existing_user.username
    }


@app.post("/agent/run")
def run_agent_endpoint(request: AgentRequest):
    result = run_agent(request.data)

    return result