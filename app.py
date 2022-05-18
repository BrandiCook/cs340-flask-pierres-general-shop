# Citation for app.py:
# Date: 05/17/2022
# Based on: OSU CS340 flask-starter-app
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json
import database.db_connector as db
import os

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database() 

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/Employees')
def employees():

    query = "SELECT * FROM Employees;"

    # The way the interface between MySQL and Flask works is by using an
    # object called a cursor. Think of it as the object that acts as the
    # person typing commands directly into the MySQL command line and
    # reading them back to you when it gets results
    cursor = db.execute_query(db_connection=db_connection, query=query)

    # The cursor.fetchall() function tells the cursor object to return all
    # the results from the previously executed
    #
    # The json.dumps() function simply converts the dictionary that was
    # returned by the fetchall() call to JSON so we can display it on the
    # page.
    results = json.dumps(cursor.fetchall())

    return results

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9286))
    app.run(port=port, debug=True)