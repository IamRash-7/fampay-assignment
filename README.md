# Setting Up

1. Clone the project

`git clone https://github.com/IamRash-7/fampay-assignment.git`

2. Activate Virtual Environment
```
cd fampay-assignment

pip3 install virtualenv

virtualenv my_env

source my_env/bin/activate
```
3. Create .env file (**All these variables are required**)
```
API_KEYS_STRING=KEY1,KEY2
MONGO_URI=mongodb://{HOST}:{PORT}/
REDIS_URI=redis://{HOST}:{PORT}/0
DATABASE_NAME=DATABASE_NAME
COLLECTION_NAME=COLLECTION_NAME
```
4. Install Requirements

`pip3 install -r requirements.txt`

# RUN in DOCKER
1. `docker-compose build`
2. `docker-compose up`

#### To Stop
`docker-compose down`

# RUN LOCALLY
*NOTE: Change .env file accordingly*
1. `python3 app.py`
2. `redis-server --port 6379`
3. `celery -A src.tasks worker --loglevel=info` - *Worker*
4. `celery -A src.tasks beat --loglevel=info` - *Scheduler*

# API ENDPOINTS
*NOTE: My Youtube query = football*
### Test Connection
* Method = **GET**
* Endpoint = **/hello**
* Example = http://127.0.0.1:8002/hello
### Get paginated Vidoes
* Method = **GET**
* Endpoint = **/videos**
* Params

    1. **page** - Required Page Number
    2. **per_page** - No. items per page

* Example = http://127.0.0.1:8002/videos?page=1&per_page=5

### Search Videos
* Method = **GET**
* Endpoint = **/search**
* Params

    1. **query** - Search text

* Example = http://127.0.0.1:8002/search?query=messi

# Tech Stack
* Python 
* Flask
* MongoDB
* Celery
* Redis
* PyMongo
* Docker

# Workflow
![alt text](https://github.com/IamRash-7/fampay-assignment/blob/main/design%20diagram2.jpeg "Logo Title Text 1")

