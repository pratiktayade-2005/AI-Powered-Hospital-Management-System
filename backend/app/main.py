from fastapi import FastAPI

from app.core.config import settings
from app.db.database import Base, engine

from app.models.patient import Patient
from app.models.user import User

from app.api.v1.patients import router as patient_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(patient_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.PROJECT_NAME} is running"
    }