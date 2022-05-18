# Citation for app.py:
# Date: 05/17/2022
# Based on: OSU CS340 flask-starter-app
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    people_from_app_py = [
        {
            "name": "Thomas",
            "age": 33,
            "location": "New Mexico",
            "favorite_color": "Blue"
        },
        {
            "name": "Gregory",
            "age": 41,
            "location": "Texas",
            "favorite_color": "Red"
        },
        {
            "name": "Vincent",
            "age": 27,
            "location": "Ohio",
            "favorite_color": "Green"
        },
        {
            "name": "Alexander",
            "age": 29,
            "location": "Florida",
            "favorite_color": "Orange"
        }
        ]
    return render_template("main.j2", people=people_from_app_py)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9286))
    app.run(port=port, debug=True)