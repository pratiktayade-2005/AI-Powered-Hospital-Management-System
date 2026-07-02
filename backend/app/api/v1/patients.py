from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.patient_repository import PatientRepository
from app.schemas.patient import PatientCreate, PatientResponse

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/", response_model=PatientResponse)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return PatientRepository.create_patient(db, patient)


@router.get("/", response_model=list[PatientResponse])
def get_all_patients(
    db: Session = Depends(get_db)
):
    return PatientRepository.get_all_patients(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = PatientRepository.get_patient_by_id(db, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: int,
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    updated_patient = PatientRepository.update_patient(
        db,
        patient_id,
        patient
    )

    if updated_patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return updated_patient


@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = PatientRepository.delete_patient(
        db,
        patient_id
    )

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }