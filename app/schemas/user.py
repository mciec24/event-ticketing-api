from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    name : str
    surname : str
    email : EmailStr
    phone_number : str


class UserResponse(BaseModel):
    id : int
    name : str
    surname : str
    email : EmailStr
    phone_number : str

    model_config = ConfigDict(from_attributes=True)