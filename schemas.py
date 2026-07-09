from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    username_or_email: str
    password: str


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str
    created_at: datetime


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"