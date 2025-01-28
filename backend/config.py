from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MONGO CRED: username: admin, password: kINNPfWffVyeulVk
uri = "mongodb+srv://admin:kINNPfWffVyeulVk@cluster0.eozxc.mongodb.net"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Create a new database, if the database does not exist
db = client.test

# Create a new collection, if the collection does not exist
collection = db["users"]

# Create a new collection, if the collection does not exist
videosCollection = db["videos"]