from config import collection, videosCollection

def create_user(user):
    # Insert a new user into the collection
    new_user = {
        "id": user.id,
        "email": user.email,
        "password": user.password,
        "videos": []
    }
    collection.insert_one(new_user)
    return {"Response": "User created successfully"}

def get_users():
    users = collection.find(
        {}, 
        {
            "password": 0
        }
    )
    return users

def get_user(email):
    user = collection.find_one({"email": email})
    return user

def update_user(email, user):
    # Update an existing user in the collection
    new_user = {
        "id": user.id,
        "email": user.email,
        "password": user.password
    }
    collection.update_one({"email": email}, {"$set": new_user})
    return {"Response": "User updated successfully"}

def delete_user(email):
    # Delete an existing user from the collection
    collection.delete_one({"email": email})
    return {"Response": "User deleted successfully"}

def create_video(video):
    # Insert a new video into the collection
    new_video = {
        "id": video.id,
        "title": video.title,
        "url": video.url,
        "user_id": video.user_id
    }
    videosCollection.insert_one(new_video)

    # Update the user's videos list
    user = collection.find_one({"id": video.user_id})
    user_videos = user.get("videos", [])
    user_videos.append(video.id)
    collection.update_one({"id": video.user_id}, {"$set": {"videos": user_videos}})

    return {"Response": "Video created successfully"}

def get_videos():
    videos = videosCollection.find()
    return videos

def get_video(video_id):
    video = videosCollection.find_one({"id": video_id})
    return video

def update_video(video_id, video):
    # Update an existing video in the collection
    new_video = {
        "id": video.id,
        "title": video.title,
        "url": video.url,
        "user_id": video.user_id
    }
    videosCollection.update_one({"id": video_id}, {"$set": new_video})
    return {"Response": "Video updated successfully"}

def delete_video(video_id):
    # Delete an existing video from the collection
    videosCollection.delete_one({"id": video_id})
    return {"Response": "Video deleted successfully"}

def get_user_videos(user_email):
    user = collection.find_one({"email": user_email})
    user_videos = user.get("videos", [])
    videos = []
    for video_id in user_videos:
        video = videosCollection.find_one({"id": video_id})
        videos.append(video)
    return videos
