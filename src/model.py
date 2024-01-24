from bson import ObjectId

# Model for Videos
class Video:
    def __init__(self, _id, title, description, published_datetime, thumbnail_url, video_id):
        self._id = ObjectId() if _id is None else _id
        self.title = title
        self.description = description
        self.published_datetime = published_datetime
        self.thumbnail_url = thumbnail_url
        self.video_id = video_id

    def to_dict(self):
        return {
            '_id': str(self._id),
            'title': self.title,
            'description': self.description,
            'published_datetime': self.published_datetime,
            'thumbnail_url': self.thumbnail_url,
            'video_id': self.video_id
        }
