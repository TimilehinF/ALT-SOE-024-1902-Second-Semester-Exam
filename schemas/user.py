from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    is_active: Optional[bool] = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

users = []