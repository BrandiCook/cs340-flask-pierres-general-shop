# Citation for db_connector.py:
# Date: 05/18/2022
# Based on: OSU cs340_starter_app
# Source URL: https://github.com/mlapresta/cs340_starter_app and https://github.com/osu-cs340-ecampus/flask-starter-app
# ---------------------------------------------------------------------------------------------------------------------

# the following will be used by the webapp.py to interact with the database
# You can also use environment variables

import os
from dotenv import load_dotenv, find_dotenv
# Load the .env file into the environment variables
load_dotenv(dotenv_path)

# Set the variables in our app to the already set environment variables
host = os.environ.get("340DBHOST")
user = os.environ.get("340DBUSER")
passwd = os.environ.get("340DBPW")
db = os.environ.get("340DB")
