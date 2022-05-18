import os
from dotenv import load_dotenv, find_dotenv
# Load the .env file into the environment variables
load_dotenv(dotenv_path)

# Set the variables in our app to the already set environment variables
host = os.environ.get("340DBHOST")
user = os.environ.get("340DBUSER")
passwd = os.environ.get("340DBPW")
db = os.environ.get("340DB")

# host = 'classmysql.engr.oregonstate.edu'  #DON'T CHANGE ME UNLESS THE INSTRUCTIONS SAY SO
# user = 'cs340_MYUSER' #CHANGE ME (I changed for privacy)
# passwd = '1111' #CHANGE ME
# db = 'cs340_MYUSER' #CHANGE ME