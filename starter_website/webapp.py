# Citation for webapp.py:
# Date: 05/18/2022
# Based on: OSU cs340_starter_app
# Source URL: https://github.com/mlapresta/cs340_starter_app and https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template
from flask import request, redirect
from flask_mysqldb import MySQL
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

mysql = MySQL(app)


@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/customers.html')
def browse_customers():
    return render_template("customers.html")

@app.route('/employees.html')
def browse_employees():
    return render_template("employees.html")

@app.route('/products.html')
def browse_products():
    return render_template("products.html")

@app.route('/orders.html')
def browse_orders():
    return render_template("orders.html")

@app.route("/customers/add", methods=["GET", "POST"])
def browse_add_customers():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query = "SELECT customerName from Customers;"
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        return render_template("customers.html", browse_add_customers=result)

    elif request.method == "POST":
        cur = mysql.connection.cursor()
        data = (request.form["certname"],)
        insert_query = "INSERT into `Customers` (customerName) VALUES (%s)"
        cur.execute(insert_query, data)
        query = "SELECT customerName from Customers"
        cur.execute(query)
        result =cur.fetchall()
        print(result)
        return render_template("customers.html", browse_add_customers=result)

@app.route("/employees/add", methods=["GET", "POST"])
def browse_add_employees():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query = "SELECT employeeName from Employees;"
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        return render_template("employees.html", browse_add_employees=result)

    elif request.method == "POST":
        cur = mysql.connection.cursor()
        data = (request.form["certname"],)
        insert_query = "INSERT into `Employees` (employeeName) VALUES (%s)"
        cur.execute(insert_query, data)
        query = "SELECT employeeName from Employees"
        cur.execute(query)
        result =cur.fetchall()
        print(result)
        return render_template("employees.html", browse_add_employees=result)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html')
