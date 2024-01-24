from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo import TEXT, ASCENDING

# SETUP DATABASE
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DATABASE_NAME]
videos_collection = db[COLLECTION_NAME]

# Index for Title and Descrtion to help with search
videos_collection.create_index([("title", TEXT), ("description", TEXT)])

# Index for Video_id
videos_collection.create_index([('video_id', ASCENDING)])
