from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: str
    email: str
    password: str
    videos: List[str] = []

class UserResponse(BaseModel):
    id: str
    email: str

class Videos(BaseModel):
    id: str
    title: str
    url: str
    user_id: str