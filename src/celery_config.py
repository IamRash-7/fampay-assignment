from kombu import Exchange, Queue
import os
from dotenv import load_dotenv

# Celery Config file
load_dotenv()
REDIS_URI = os.getenv("REDIS_URI")

BROKER_URL = REDIS_URI
CELERY_RESULT_BACKEND = REDIS_URI
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)
