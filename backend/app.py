from fastapi import FastAPI
from database import engine, Base

app = FastAPI(title="AI Dataset Labeling Marketplace")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Dataset Labeling Marketplace Backend"
    }
