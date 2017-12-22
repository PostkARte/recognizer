# 1 Setup
##  1.1 Docker
 1. Navigate to the root directory of the project.
 2. Build the docker container with  `docker-compose build`
 3. Run the docker container with `docker-compose up`
 4. Remove the docker container with  `docker-compose down`
## 1.2 Python
 1. Install Python 3.6
 2. Navigate to the root directory of the project.
 3. Install the needed requirements with `pip install -r requirements.txt`
 4. Start the server with the following command `gunicorn PostkARteRecognizer.wsgi --bind 0.0.0.0:8000 --workers 3`
# 2 Usage
## 2.1 Saving a new postcard
**Urlpattern**: `http://<ip>/recognizer/save/`
**Form-Data-Parameters**: id; file

## 2.2 Matching a postcard
**Urlpattern**: `http://<ip>/recognizer/match/`
**Form-Data-Parameters**: file

## 2.2 Show recognizable postcards
**Urlpattern**: `http://<ip>/recognizer/postcards/`
