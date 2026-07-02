from pydantic import BaseModel, EmailStr


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    phone: str
    email: EmailStr


class PatientResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    gender: str
    phone: str
    email: EmailStr

    class Config:
        from_attributes = True