from flask import Flask
from src.api import api_blueprint

# Initialize Flask app and MongoDB client
app = Flask(__name__)

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8002)

# docker-compose build
# docker-compose up
# docker-compose down