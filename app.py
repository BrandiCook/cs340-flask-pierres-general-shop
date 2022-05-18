# Citation for app.py:
# Date: 05/17/2022
# Based on: OSU CS340 flask-starter-app
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
# app.config['MYSQL_USER'] = 'cs340_cookb4'
# app.config['MYSQL_PASSWORD'] = '9286' #last 4 of onid
# app.config['MYSQL_DB'] = 'cs340_cookb4'
# app.config['MYSQL_CURSORCLASS'] = "DictCursor"


# mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    return "Welcome to the OSU CS 340 - Flask Tutorial!"


# Listener
if __name__ == "__main__":

    #Start the app on port 9287
    port = int(os.environ.get('PORT', 9287))
    app.run(port=port, debug=True)