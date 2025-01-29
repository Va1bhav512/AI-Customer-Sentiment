from fastapi import FastAPI
import uvicorn
from config import collection
from routes.user import router as userRouter
from routes.ai import router as aiRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Based Sentiment Analysis",
    description="A simple API to register, login user, add reviews and perform sentiment analysis on text data",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(userRouter)
app.include_router(aiRouter)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)