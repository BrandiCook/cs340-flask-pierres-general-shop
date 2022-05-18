from flask import Flask, render_template, json, request, redirect
from flask_mysqldb import MySQL
from flask import request
import database.db_connector as db
import os

# Configuration

app = Flask(__name__)

# app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
# app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
# app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
# app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
# app.config["MYSQL_CURSORCLASS"] = os.environ.get("MYSQL_CURSORCLASS")

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_cookb4'
app.config['MYSQL_PASSWORD'] = '9286' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_cookb4'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# connect to db
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/bsg-people')
def bsg_people():
    query = "SELECT * FROM bsg_people;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("bsg.j2", bsg_people=results)
# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9287)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 