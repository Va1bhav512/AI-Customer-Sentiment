from pydantic import BaseModel
from typing import List


class Review(BaseModel):
        content: str
        created_at: str
        class AnalysisModel(BaseModel):
            sentiment: str
            emotion: str
            keyThemes: List[str]
            painPoints: List[str]
            urgency: str
            recommendation: List[str]
        analysis: AnalysisModel

class User(BaseModel):
    cname: str
    email: str
    password: str
    reviews: List[Review] = []


class UserResponse(BaseModel):
    cname: str
    email: str
    reviews: List[Review] = []

class UserSignIn(BaseModel):
    email: str
    password: str