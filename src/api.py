import json
from bson import json_util
from src.model import Video
from math import ceil
from src.database import videos_collection
from flask import jsonify, request, Blueprint

api_blueprint = Blueprint('api', __name__)

# Helper Functions
def parse_json(data):
    return json.loads(json_util.dumps(data))

def get_pagination_data(page, per_page):
    total_items = videos_collection.count_documents({})
    response = {
        "page": page,
        "page_size": per_page,
        "total_items": total_items,
        "total_pages": ceil(total_items/per_page)
    }
    return response

# SERVER
@api_blueprint.route('/hello', methods=['GET'])
def hello():
    return {"Message":"Hello"}

# Get paginated video data
@api_blueprint.route('/videos', methods=['GET'])
def get_videos():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    videos = videos_collection.find().sort('published_datetime', -1).skip((page - 1) * per_page).limit(per_page)

    videos = parse_json(videos)
    videos_list = [Video(**video).to_dict() for video in videos]
    pagination_data = get_pagination_data(page, per_page)

    return jsonify({'videos': videos_list} | (pagination_data))

# Search videos
@api_blueprint.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query', '')

    videos = videos_collection.find({"$text": {"$search": query}}).sort('published_datetime', -1)

    videos = parse_json(videos)
    videos_list = [Video(**video).to_dict() for video in videos]
    return jsonify({'videos': videos_list})