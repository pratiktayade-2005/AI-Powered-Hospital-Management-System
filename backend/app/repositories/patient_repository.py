from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate


class PatientRepository:

    @staticmethod
    def create_patient(db: Session, patient: PatientCreate):

        new_patient = Patient(
            first_name=patient.first_name,
            last_name=patient.last_name,
            age=patient.age,
            gender=patient.gender,
            phone=patient.phone,
            email=patient.email
        )

        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)

        return new_patient

    @staticmethod
    def get_all_patients(db: Session):
        return db.query(Patient).all()

    @staticmethod
    def get_patient_by_id(db: Session, patient_id: int):
        return db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

    @staticmethod
    def delete_patient(db: Session, patient_id: int):

        patient = db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

        if patient:
            db.delete(patient)
            db.commit()

        return patient

    @staticmethod
    def update_patient(db: Session, patient_id: int, patient_data: PatientCreate):

        patient = db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

        if patient:

            patient.first_name = patient_data.first_name
            patient.last_name = patient_data.last_name
            patient.age = patient_data.age
            patient.gender = patient_data.gender
            patient.phone = patient_data.phone
            patient.email = patient_data.email

            db.commit()
            db.refresh(patient)

        return patient