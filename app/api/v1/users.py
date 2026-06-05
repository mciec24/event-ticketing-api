from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserResponse, UserCreate
from services.user_service import UserAlreadyExistsError
from sqlalchemy.orm import Session
from db.database import get_db
from services import user_service

router = APIRouter(prefix="/users", tags = ["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db : Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))