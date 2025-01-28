from fastapi import APIRouter, HTTPException
from database.schemas import create_user, get_users, get_user, update_user, delete_user, get_user_videos
from database.models import User


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
async def read_users():
    users = get_users()
    response = []
    for user in users:
        print(user)
        thisResponse = {
            "id": user["id"],
            "email": user["email"],
            "videos": user["videos"]
        }
        response.append(thisResponse)
    return response

@router.get("/{email}")
async def read_user(email: str):
    user = get_user(email)
    if user:
        response = {
            "id": user["id"],
            "email": user["email"],
            "videos": user["videos"]
        }
        return response
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/")
async def create_user_route(user: User):
    user = create_user(user)
    return user

@router.put("/{email}")
async def update_user_route(email: str, user: User):
    user = update_user(email, user)
    return user

@router.delete("/{email}")
async def delete_user_route(email: str):
    user = delete_user(email)
    return user

@router.get("/{email}/videos")
async def read_user_videos(email: str):
    videos = get_user_videos(email)
    response = []
    for video in videos:
        thisResponse = {
            "id": video["id"],
            "title": video["title"],
            "url": video["url"],
            "user_id": video["user_id"]
        }
        response.append(thisResponse)
    return response