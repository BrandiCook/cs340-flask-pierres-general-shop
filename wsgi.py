# file for gunicorn

# Citation for wsgi.py:
# Date: 05/17/2022
# Based on: OSU CS340 flask-starter-app
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from app import app

if __name__ == "__main__":
    app.run()