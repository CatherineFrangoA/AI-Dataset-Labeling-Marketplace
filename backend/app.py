from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent
from api.user import router as user_router

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


@app.get("/")
def home():
    return "AI Dataset Labeling Marketplace"


@app.post("/agent/run")
def run_agent_endpoint(request: dict):
    result = run_agent(request["data"])
    return result