# Citation for webapp.py:
# Date: 05/18/2022
# Based on: OSU cs340_starter_app
# Source URL: https://github.com/mlapresta/cs340_starter_app and https://github.com/osu-cs340-ecampus/flask-starter-app
# Portions copied or adapted from: https://canvas.oregonstate.edu/courses/1870053/pages/exploration-developing-in-flask?module_item_id=22036042 

from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL
import os
import database.db_connector as db


# Configuration

app = Flask(__name__)
# db_connection = db.connect_to_database()

app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_cookb4"
app.config["MYSQL_PASSWORD"] = "9286"
app.config["MYSQL_DB"] = "cs340_cookb4"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


# @app.route('/home')
# def index():
#     return render_template("home.j2", title="Home")

# @app.route('/')
# def home():
#     return render_template("home.j2", title="Home")

@app.route('/home')
def index():
    return render_template("home.j2")

@app.route('/')
def home():
    return render_template('home.j2')


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    # Separate out the request methods, in this case this is for a POST
    # insert a person into the Employees entity
    if request.method == "POST":
        # fire off if user presses the Add Employee button
        if request.form.get("Add_Employee"):
            # grab user form inputs
            employeeName = request.form["employeeName"]
            employeeSalary = request.form["employeeSalary"]

            # account for null salary
            if employeeSalary == "":
                # mySQL query to insert a new person into Employees with our form inputs
                query = "INSERT INTO Employees (employeeName) VALUES (%s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (employeeName))
                mysql.connection.commit()

            # account for null name
            elif employeeName == "":
                query = "INSERT INTO Employees (employeeSalary) VALUES (%s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (employeeSalary))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO Employees (employeeName, employeeSalary) VALUES (%s,%s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (employeeName, employeeSalary))
                mysql.connection.commit()

            # redirect back to employees page
            return redirect("/employees")

    # Grab data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the employees in our database
        query = "SELECT * FROM Employees;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_employeespage passing our query data and employee data to the edit_employee template
        return render_template("employees.j2", data=data)

@app.route("/delete_employee/<int:id>")
def delete_employee(id):
    # mySQL query to delete the employee with our passed id
    query = "DELETE FROM Employees WHERE employeeID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to employees page
    return redirect("/employees")

# route for edit functionality, updating the attributes of a person in Employees
# similar to our delete route, we want to the pass the 'id' value of that employee on button 
@app.route("/edit_employees/<int:id>", methods=["POST", "GET"])
def edit_employees(id):
    if request.method == "GET":
        # mySQL query to grab the info 
        query = "SELECT * FROM Employees WHERE employeeID = %s ;" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit_employees.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_Employee"):
            # grab user form inputs
            employeeID = request.form["employeeID"]
            employeeName = request.form["employeeName"]
            employeeSalary = request.form["employeeSalary"]

            # account for null salary
            if (employeeSalary == "" or employeeSalary == "None"):
                # mySQL query to update the attributes of person with our passed id value
                query = "UPDATE Employees SET employeeName = %s, employeeSalary = NULL WHERE employeeID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (employeeName, employeeID))
                mysql.connection.commit()

            # account for null name
            elif (employeeName == "" or employeeName == "None"):
                query = "UPDATE Employees SET employeeName = NULL, employeeSalary = %s WHERE employeeID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (employeeSalary, employeeID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Employees SET employeeName = %s, employeeSalary = %s WHERE employeeID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (employeeName, employeeSalary, employeeID))
                mysql.connection.commit()

            # redirect back to employees page after we execute the update query
            return redirect("/employees")


# route for people page
@app.route("/customers", methods=["POST", "GET"])
def customers():
    # Separate out the request methods, in this case this is for a POST
    # insert a person into the Customers entity
    if request.method == "POST":
        # fire off if user presses the Add Customer button
        if request.form.get("Add_Customer"):
            # grab user form inputs
            customerName = request.form["customerName"]
            dateOfBirth = request.form["dateOfBirth"]
            favoriteProduct = request.form["favoriteProduct"]

            # account for null age AND favoriteProduct
            if dateOfBirth == "" and favoriteProduct == "":
                # mySQL query to insert a new person into Customers with our form inputs
                query = "INSERT INTO Customers (customerName) VALUES (%s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName))
                mysql.connection.commit()

            # account for null favoriteProduct
            elif favoriteProduct == "0":
                query = "INSERT INTO Customers (customerName, dateOfBirth) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, dateOfBirth))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO Customers (customerName, dateOfBirth, favoriteProduct) VALUES (%s, %s,%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, dateOfBirth, favoriteProduct))
                mysql.connection.commit()

            # redirect back to people page
            return redirect("/customers")

    # Grab Customers data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the people in Customers
        query = "SELECT * FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and favoriteProduct data to the edit_people template
        return render_template("customers.j2", data=data)

@app.route("/delete_customer/<int:id>")
def delete_customer(id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Customers WHERE customerID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to customers page
    return redirect("/customers")

@app.route("/edit_customers/<int:id>", methods=["POST", "GET"])
def edit_customers(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed customerID
        query = "SELECT * FROM Customers WHERE customerID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_customers page passing our query data and favoriteProduct data to the edit_customers template
        return render_template("edit_customers.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_Customer"):
            # grab user form inputs
            customerID = request.form["customerID"]
            customerName = request.form["customerName"]
            dateOfBirth = request.form["dateOfBirth"]
            favoriteProduct = request.form["favoriteProduct"]

            # account for null age AND favoriteProduct
            if dateOfBirth == "" and favoriteProduct == "":
                # mySQL query to update the attributes of person with our passed customerID value
                query = "UPDATE Customers SET customerName = %s, dateOfBirth = NULL, favoriteProduct = NULL WHERE customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, dateOfBirth, customerID))
                mysql.connection.commit()

            # account for null favoriteProduct
            elif (favoriteProduct == "" or favoriteProduct=="") :
                query = "UPDATE Customers SET customerName = %s, dateOfBirth = %s, favoriteProduct = NULL WHERE customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, dateOfBirth, customerID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Customers SET customerName = %s, dateOfBirth = %s, favoriteProduct = %s WHERE customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, dateOfBirth, favoriteProduct, customerID))
                mysql.connection.commit()

            # redirect back to customers page after we execute the update query
            return redirect("/customers")

# route for products page
@app.route("/products", methods=["POST", "GET"])
def products():
    # Separate out the request methods, in this case this is for a POST
    # insert a product into the Products entity
    if request.method == "POST":
        # fire off if user presses the Add Product button
        if request.form.get("Add_Product"):
            # grab user form inputs
            productName = request.form["productName"]
            productDescription = request.form["productDescription"]
            productPrice = request.form["productPrice"]
            seasonSold = request.form["seasonSold"]

            # account for null productDescription
            if productDescription == "":
                # mySQL query to insert a new product into Products with our form inputs
                query = "INSERT INTO Products (productName, productPrice, seasonSold) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (productName, productPrice, seasonSold))
                mysql.connection.commit()
            
            # no NULL values option
            else:
                query = "INSERT INTO Products (productName, productDescription, productPrice, seasonSold) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (productName, productDescription, productPrice, seasonSold))
                mysql.connection.commit()

            # redirect back to products page
            return redirect("/products")

    if request.method == "GET":
        # mySQL query to grab all the products in Products
        query = "SELECT * from Products"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("products.j2", data=data)

# route to search products by season
@app.route("/search_products", methods=["GET"])
def search_products():

    if request.method == "GET":

        season = request.args.get('seasonSold')
        # mySQL query to grab all the products in Products by season sold
        query = "SELECT * from Products WHERE seasonSold = '%s'" % season
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("search_products.j2", data=data, season = season)

# route for delete functionality, deleting a product from Products,
# we want to pass the 'id' value of that product on button click (see HTML) via the route
@app.route("/delete_product/<int:id>")
def delete_product(id):
    # mySQL query to delete the product with our passed id
    query = "DELETE FROM Products WHERE productID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to products page
    return redirect("/products")

# route for edit functionality, updating the attributes of a product in Products
# similar to our delete route, we want to the pass the 'id' value of that product on button click (see HTML) via the route
@app.route("/edit_products/<int:id>", methods=["POST", "GET"])
def edit_products(id):
    if request.method == "GET":
        # mySQL query to grab the info of the product with our passed id
        query = "SELECT * FROM Products WHERE productID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_products page passing our query data and homeworld data to the edit_products template
        return render_template("edit_products.j2", data=data)

    if request.method == "POST":
        # fire off if user clicks the 'Edit Product' button
        if request.form.get("Edit_Product"):
            # grab user form inputs
            productID = request.form["productID"]
            productName = request.form["productName"]
            productDescription = request.form["productDescription"]
            productPrice = request.form["productPrice"]
            seasonSold = request.form["seasonSold"]
            # account for null productDescription
            
            # account for null productDescription
            if (productDescription == "" or productDescription == "None"):
                # mySQL query to update a product into Products with our form inputs
                query = "UPDATE Products SET productName = %s, productDescription = NULL, productPrice = %s, seasonSold = %s WHERE productID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (productName, productPrice, seasonSold, productID))
                mysql.connection.commit()
            
            # no NULL values option
            else:
                query = "UPDATE Products SET productName = %s, productDescription = %s, productPrice = %s, seasonSold = %s WHERE productID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (productName, productDescription, productPrice, seasonSold, productID))
                mysql.connection.commit()

            

            # redirect back to products page
            return redirect("/products")
# route for orders page
@app.route("/orders", methods=["POST", "GET"])
def orders():
    # Separate out the request methods, in this case this is for a POST
    # insert a order into the Orders entity
    if request.method == "POST":
        # fire off if user presses the Add Order button
        if request.form.get("Add_Order"):

            # grab user form inputs
            orderDate = request.form["orderDate"]
            orderPrice = request.form["orderPrice"]
            customerID = request.form["customerName"]
            employeeID = request.form["employeeName"]
            
            # account for null customerID AND employeeID
            if customerID == "0" and employeeID == "0":
                # mySQL query to insert a new order into Orders with our form inputs
                query = "INSERT INTO Orders (orderDate, orderPrice) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (orderDate, orderPrice))
                mysql.connection.commit()

            # account for null customerID
            elif customerID == "0":
                query = "INSERT INTO Orders (orderDate, orderPrice, employeeID) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (orderDate, orderPrice, employeeID))
                mysql.connection.commit()

            # account for null employeeID
            elif employeeID == "0":
                query = "INSERT INTO Orders (orderDate, orderPrice, customerID) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (orderDate, orderPrice, customerID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO Orders (orderDate, orderPrice, customerID, employeeID) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (orderDate, orderPrice, customerID, employeeID))
                mysql.connection.commit()

            # redirect back to order page
            return redirect("/orders")
        
        # fire off if user presses the Add Order Details button
        elif request.form.get("Add_Order_Detail"):
            
            # grab user form inputs
            orderID = request.form["orderID"]
            productID = request.form["productID"]

            # Account for NULL productID
            if productID == "0":
                query = "INSERT INTO OrderDetails (orderID) VALUES (%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (orderID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO OrderDetails (orderID, productID) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (orderID, productID))
                mysql.connection.commit()

            # redirect back to order page
            return redirect("/orders")

    if request.method == "GET":
        # mySQL query to grab all the orders in Orders
        query = "SELECT Orders.orderID, orderDate, orderPrice, Customers.customerName, Employees.employeeName FROM Orders LEFT JOIN Customers ON Orders.customerID = Customers.customerID LEFT JOIN Employees ON Orders.employeeID = Employees.employeeID ORDER BY orderID ASC;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        order_data = cur.fetchall()

        # mySQL query to grab all the order details in OrderDetails
        query2 = "SELECT orderDetailID, orderID, OrderDetails.productID, Products.productName FROM OrderDetails LEFT JOIN Products ON OrderDetails.productID = Products.productID;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        order_details_data = cur.fetchall()

        # mySQL query to get all Customer IDs and Customer Names to populate customerName dropdown
        query3 = "SELECT customerID, customerName FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        customer_names = cur.fetchall()

        # mySQL query to get all Employee IDs and Employee Names to populate employeeName dropdown
        query4 = "SELECT employeeID, employeeName FROM Employees;"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        employee_names = cur.fetchall()

        # mySQL query to get all Product IDs and Product Names to populate productName dropdown
        query5 = "SELECT productID, productName FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query5)
        product_names = cur.fetchall()

        return render_template("orders.j2", order_data=order_data, order_details_data=order_details_data, customer_names=customer_names, employee_names=employee_names, product_names=product_names)

# route for edit functionality, updating the attributes of a order detail in OrderDetails
@app.route("/edit_order_detail/<int:id>", methods=["POST", "GET"])
def edit_order_detail(id):
    if request.method == "GET":
        # mySQL query to grab the info of the order detail with our passed id
        query = "SELECT * FROM OrderDetails WHERE orderDetailID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to get all Product IDs and Product Names to populate productName dropdown
        query2 = "SELECT productID, productName FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        product_names = cur.fetchall()

        # mySQL query to get all current order IDs to populate orderID dropdown
        query3 = "SELECT orderID FROM Orders;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        order_id = cur.fetchall()

        return render_template("edit_order_detail.j2", data=data, product_names=product_names, order_id=order_id)

    if request.method == "POST":
        # fire off if user clicks the 'Edit Order Detail' button
        if request.form.get("Edit_Order_Detail"):
            # grab user form inputs
            orderDetailID = request.form["orderDetailID"]
            orderID = request.form["orderID"]
            productID = request.form["productID"]

            # account for NULL productID
            if productID == "0":
                query = "UPDATE OrderDetails SET orderID = %s, productID = NULL WHERE orderDetailID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, ( orderID, orderDetailID ))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE OrderDetails SET orderID = %s, productID = %s WHERE orderDetailID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, ( orderID, productID, orderDetailID ))
                mysql.connection.commit()

            # redirect back to products page
            return redirect("/orders")

# route for edit functionality, updating the attributes of a order in Orders
@app.route("/edit_order/<int:id>", methods=["POST", "GET"])
def edit_order(id):
    if request.method == "GET":
        # mySQL query to grab the info of the order with our passed id
        query = "SELECT * FROM Orders WHERE orderID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to get all Customer IDs and Customer Names to populate customerName dropdown
        query2 = "SELECT customerID, customerName FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customerName = cur.fetchall()

        # mySQL query to get all Employee IDs and Employee Names to populate employeeName dropdown
        query3 = "SELECT employeeID, employeeName FROM Employees;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        employeeName = cur.fetchall()

        # render edit_order page passing our query data and customer and employee data to the edit_order template
        return render_template("edit_order.j2", data=data, customerName=customerName, employeeName=employeeName)

    if request.method == "POST":
        # fire off if user clicks the 'Edit Order' button
        if request.form.get("Edit_Order"):
            # grab user form inputs
            orderID = request.form["orderID"]
            orderDate = request.form["orderDate"]
            orderPrice = request.form["orderPrice"]
            customerID = request.form["customerName"]
            employeeID = request.form["employeeName"]

            # account for null customerID AND employeeID
            if customerID == "0" and employeeID == "0":
                query = "UPDATE Orders SET orderDate = %s, orderPrice = %s, customerID = NULL, employeeID = NULL WHERE orderID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, ( orderDate, orderPrice, orderID ))
                mysql.connection.commit()

            # account for null customerID
            elif customerID == "0":
                query = "UPDATE Orders SET orderDate = %s, orderPrice = %s, customerID = NULL, employeeID = %s WHERE orderID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, ( orderDate, orderPrice, employeeID, orderID ))
                mysql.connection.commit()

            # account for null employeeID
            elif employeeID == "0":
                query = "UPDATE Orders SET orderDate = %s, orderPrice = %s, customerID = %s, employeeID = NULL WHERE orderID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, ( orderDate, orderPrice, customerID, orderID ))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Orders SET orderDate = %s, orderPrice = %s, customerID = %s, employeeID = %s WHERE orderID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, ( orderDate, orderPrice, customerID, employeeID, orderID ))
                mysql.connection.commit()

            # redirect back to products page
            return redirect("/orders")

# route for delete functionality, deleting a product from Products,
# we want to pass the 'id' value of that product on button click (see HTML) via the route
@app.route("/delete_order/<int:id>")
def delete_order(id):
    # mySQL query to delete the order with our passed id
    query = "DELETE FROM Orders WHERE orderID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to products page
    return redirect("/orders")

# route for delete functionality, deleting a product from Products,
# we want to pass the 'id' value of that product on button click (see HTML) via the route
@app.route("/delete_order_details/<int:id>")
def delete_order_details(id):
    # mySQL query to delete the product with our passed id
    query = "DELETE FROM OrderDetails WHERE orderDetailID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to products page
    return redirect("/orders")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html')

