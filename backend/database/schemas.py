from config import collection

def create_user(user):
    # Insert a new user into the collection
    new_user = {
        "cname": user.cname,
        "email": user.email,
        "password": user.password,
        "reviews": []
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
        "cname": user.cname,
        "email": user.email,
        "password": user.password,
        "reviews": user.reviews
    }
    collection.update_one({"email": email}, {"$set": new_user})
    return {"Response": "User updated successfully"}

def delete_user(email):
    # Delete an existing user from the collection
    collection.delete_one({"email": email})
    return {"Response": "User deleted successfully"}

def add_review(email, review):
    # Add a review to a user's reviews
    user = collection.find_one({"email": email})
    user_reviews = user["reviews"]
    user_reviews.append(review)
    collection.update_one({"email": email}, {"$set": {"reviews": user_reviews}})
    return {"Response": "Review added successfully"}