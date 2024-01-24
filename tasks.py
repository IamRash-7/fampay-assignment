from celery import Celery, schedules
from googleapiclient.discovery import build
from datetime import datetime
import os
from dotenv import load_dotenv
from model import Video
from database import videos_collection

# Setup Celery
app = Celery('tasks')
app.config_from_object('celery_config')

# Load Variables
load_dotenv()
API_KEYS_STRING = os.getenv("API_KEYS_STRING")
API_KEYS = API_KEYS_STRING.split(',')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

expired_keys = []

# Fetch Videos and Supplying multiple API Keys in case of failure
def fetch_videos():
    response = []
    for API_KEY in API_KEYS:
        if API_KEY in expired_keys:
            continue
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
        try:
            response = youtube.search().list(q='football', part='snippet', type='video', order='date', maxResults=10).execute()
            break
        except:
            expired_keys.append(API_KEY)
            print("Trying another KEY")
    
    if response == []:
        raise Exception("Invalid API KEYS")
    
    return response

@app.task
def fetch_and_store_videos():
    response = fetch_videos()
    new_videos_list = []
    for item in response['items']:
        # Data from API
        title = item['snippet']['title']
        description = item['snippet']['description']
        published_datetime = datetime.strptime(item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
        thumbnail_url = item['snippet']['thumbnails']['default']['url']
        video_id = item['id']['videoId']

        # Ignore Video if it already exists
        existing_video = videos_collection.find({"video_id":video_id})
        existing_video = list(existing_video)
        if len(existing_video) != 0:
            continue
        
        # Use Model and create object
        new_video = Video(title = title, description = description, published_datetime = published_datetime, thumbnail_url = thumbnail_url, video_id = video_id, _id = None)
        new_video = new_video.to_dict()
        new_videos_list.append(new_video)

    if new_videos_list == []:
        print("All Videos Already Present")
    else:
        # Insert All created objects at once
        result = videos_collection.insert_many(new_videos_list)
        inserted_ids = [str(id_) for id_ in result.inserted_ids]
        print("INSERTED " + str(len(inserted_ids)) + " DOCUMENTS")


# Schedule the task to run every 30 seconds
app.conf.beat_schedule = {
    'fetch-and-store-videos': {
        'task': 'tasks.fetch_and_store_videos',
        'schedule': schedules.crontab(minute='*/1'),
    },
}
