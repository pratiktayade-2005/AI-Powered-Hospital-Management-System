from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped,mapped_column

from app.db.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)

    first_name: Mapped[str] = mapped_column(String(100),nullable=False)

    last_name: Mapped[str] = mapped_column(String(100),nullable=False)

    age: Mapped[int]

    gender: Mapped[str] = mapped_column(String(20))

    phone: Mapped[str] = mapped_column(String(15),unique=True)

    email: Mapped[str] = mapped_column(String(100),unique=True)
