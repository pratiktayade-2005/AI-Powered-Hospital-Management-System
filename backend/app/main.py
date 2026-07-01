from fastapi import FastAPI

from app.core.config import settings
from app.db.database import Base,engine

from app.models.patient import Patient

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message":f"{settings.PROJECT_NAME} is runnng"
    }