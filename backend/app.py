from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agent import run_agent
from database import Base, engine

from models.user import User
from models.dataset import Dataset
from models.label_task import LabelTask

from api.user import router as user_router
from api.dataset import router as dataset_router
from api.task import router as task_router
from api.review import router as review_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Dataset Labeling Marketplace")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/api")
app.include_router(dataset_router)
app.include_router(task_router)
app.include_router(review_router)


@app.get("/")
def home():
    return "AI Dataset Labeling Marketplace"


@app.post("/agent/run")
def run_agent_endpoint(request: dict):
    result = run_agent(request["data"])
    return result