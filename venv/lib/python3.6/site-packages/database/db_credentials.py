# To actually have your app use this file, you need to RENAME the file to db_credentials.py
# You will find details about your CS340 database credentials on Canvas.

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
