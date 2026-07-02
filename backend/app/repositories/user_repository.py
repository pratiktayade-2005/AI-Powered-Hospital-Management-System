from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate,
        hashed_password: str
    ):
        new_user = User(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            hashed_password=hashed_password,
            role=user.role
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def get_user_by_username(
        db: Session,
        username: str
    ):
        return db.query(User).filter(
            User.username == username
        ).first()

    @staticmethod
    def get_user_by_email(
        db: Session,
        email: str
    ):
        return db.query(User).filter(
            User.email == email
        ).first()

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int
    ):
        return db.query(User).filter(
            User.id == user_id
        ).first()