from fastapi import APIRouter, HTTPException
from database.schemas import create_video, get_videos, get_video, update_video, delete_video
from database.models import Videos

router = APIRouter(
    prefix="/video",
    tags=["video"]
)

@router.get("/")
async def read_videos():
    videos = get_videos()
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

@router.get("/{video_id}")
async def read_video(video_id: str):
    video = get_video(video_id)
    if video:
        response = {
            "id": video["id"],
            "title": video["title"],
            "url": video["url"],
            "user_id": video["user_id"]
        }
        return response
    raise HTTPException(status_code=404, detail="Video not found")

@router.post("/")
async def create_video_route(video: Videos):
    video = create_video(video)
    return video

@router.put("/{video_id}")
async def update_video_route(video_id: str, video: Videos):
    video = update_video(video_id, video)
    return video

@router.delete("/{video_id}")
async def delete_video_route(video_id: str):
    video = delete_video(video_id)
    return video