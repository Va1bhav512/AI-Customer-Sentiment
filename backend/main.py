from fastapi import FastAPI
import uvicorn
from config import collection
from routes.user import router as userRouter

app = FastAPI(
    title="Video Sharing API",
    description="A simple API to share videos",
    version="0.1",
    summary="Video Sharing API"
)

app.include_router(userRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)