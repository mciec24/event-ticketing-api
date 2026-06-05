from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from models.user import User
from fastapi import HTTPException

class UserAlreadyExistsError(Exception):
    pass


def create_user(db : Session, user_data : UserCreate) -> User:
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise UserAlreadyExistsError("This email address is already registered!")
    
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
