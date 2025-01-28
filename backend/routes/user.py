from fastapi import APIRouter, HTTPException
from database.schemas import create_user, get_users, get_user, update_user, delete_user, add_review, verify_user
from database.models import User, Review, UserSignIn


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
            "cname": user["cname"],
            "email": user["email"],
            "reviews": user["reviews"]
        }
        response.append(thisResponse)
    return response

@router.get("/{email}")
async def read_user(email: str):
    user = get_user(email)
    if user:
        response = {
            "cname": user["cname"],
            "email": user["email"],
            "reviews": user["reviews"]
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

# @router.get("/{email}/videos")
# async def read_user_videos(email: str):
#     videos = get_user_videos(email)
#     response = []
#     for video in videos:
#         thisResponse = {
#             "id": video["id"],
#             "title": video["title"],
#             "url": video["url"],
#             "user_id": video["user_id"]
#         }
#         response.append(thisResponse)
#     return response

@router.post("/{email}/review")
async def new_review(email: str, review: Review):
    new_review = {
        "content": review.content,
        "created_at": review.created_at,
        "analysis": {
            "sentiment": review.analysis.sentiment,
            "emotion": review.analysis.emotion,
            "keyThemes": [],
            "painPoints": [],
            "urgency": review.analysis.urgency,
            "recommendation": []
        }
    }

    for theme in review.analysis.keyThemes:
        new_review["analysis"]["keyThemes"].append(theme)
    for pain in review.analysis.painPoints:
        new_review["analysis"]["painPoints"].append(pain)
    for rec in review.analysis.recommendation:
        new_review["analysis"]["recommendation"].append(rec)

    review = add_review(email, new_review)
    return {"Response": "Review added successfully"}

@router.post("/signin")
async def signin(user: UserSignIn):
    user = verify_user(user.email, user.password)
    if user:
        response = {
            "cname": user["cname"],
            "email": user["email"],
            "reviews": user["reviews"]
        }
        return response
    raise HTTPException(status_code=404, detail="User not found")