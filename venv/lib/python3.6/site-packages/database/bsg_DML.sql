-- Read Operations
-- Note: Operations with colon : character being used to denote the
-- variables that will have data from the backend programming language

-- Select for Employees
SELECT * FROM Employees;

-- Select for Customers
SELECT customerID, customerName, dateOfBirth, Products.productName AS favoriteProduct FROM Customers INNER JOIN Products ON Customers.favoriteProduct = Products.productID;

-- Select for Products
SELECT * FROM Products;

-- Select for Products search based off of seasonSold
SELECT * FROM Products
WHERE seasonSold = :seasonSold_input_from_dropdown;

-- Select for Orders search based off of orderDate
SELECT * FROM Orders
WHERE orderDate = :orderDate_input_from_dropdown;

-- Select for Orders
SELECT Orders.orderID, orderDate, orderPrice, Customers.customerName, Employees.employeeName FROM Orders 
INNER JOIN Customers ON Orders.customerID = Customers.customerID 
INNER JOIN Employees ON Orders.employeeID = Employees.employeeID 
ORDER BY orderID ASC;

-- Select OrderDetails
SELECT orderDetailID, orderID, OrderDetails.productID, Products.productName 
FROM OrderDetails
INNER JOIN Products ON OrderDetails.productID = Products.productID;

-- Create Operations

-- Create Employee
INSERT INTO Employees (employeeName, employeeSalary)
VALUES (:employeeNameInput, employeeSalaryInput);

-- get all Product IDs and Product Names to populate favoriteProduct dropdown
SELECT productID, productName FROM Products;

-- Create Customer
INSERT INTO Customers (customerName, dateOfBirth, favoriteProduct)
VALUES (:customerNameInput, :dateOfBirthInput, :favoriteProduct_id_from_dropdown_input);

-- Create Product
INSERT INTO Products (productName, productDescription, productPrice, seasonSold)
VALUES (:productNameInput, :productDescriptionInput, :productPriceInput, :seasonSoldInput);

-- Create Order Detail
INSERT INTO OrderDetails (orderID, productID)
VALUES (:orderIDInput, :productIDInput);

-- Get all Customer IDs and Customer Names to populate customerName dropdown
SELECT customerID, customerName FROM Customers;

-- Get all Employee IDs and Employee Names to populate employeeName dropdown
SELECT employeeID, employeeName FROM Employees;

-- Create Order
INSERT INTO Orders (orderDate, orderPrice, customerName, employeeName)
VALUES (:orderDateInput, :orderPrice, :customer_id_from_dropdown_input, :employee_id_from_dropdown_input );

-- Delete Operations
-- Delete Employee
DELETE FROM Employees WHERE employeeID = :employee_ID_selected_from_browse_employees_page;

-- Delete Customer
DELETE FROM Customers WHERE customerID = :customer_ID_selected_from_browse_customers_page;

-- Delete Product
DELETE FROM Products WHERE productID = :product_ID_selected_from_browse_products_page;

-- Delete Order
DELETE FROM Orders WHERE orderID = :order_ID_selected_from_browse_orders_page;

-- Delete Order Detail
DELETE FROM OrderDetails WHERE orderDetailID = :orderDetail_ID_selected_from_browse_orderdetails_page;

-- Update Operations
-- Update Employee
-- Get information for update on click of edit
SELECT employeeID, employeeName, employeeSalary
FROM Employees
WHERE employeeID = :employee_ID_selected_from_browse_employees_page;

-- Update Employee information with input
UPDATE Employees 
  SET employeeName = :employeeNameInput,    employeeSalary = :employeeSalaryInput
  WHERE employeeID = :employee_ID_selected_from_browse_employees_page;

-- Update Customer
-- Get information for update on click of edit
SELECT customerID, customerName, dateOfBirth, Products.productName AS favoriteProduct
FROM Customers
INNER JOIN Products ON Customers.favoriteProduct = Products.productID
WHERE customerID = customer_ID_selected_from_browse_employees_page;

-- Update Customer information with input
UPDATE Customers
SET customerName = :customerNameInput, dateOfBirth = :dateOfBirthInput, favoriteProduct = favoriteProductInputFromDropdown
WHERE customerID = customer_ID_selected_from_browse_employees_page;

-- Update Order Details
-- Get information for update on click of edit
SELECT orderDetailID, orderID, productID
FROM OrderDetails
WHERE orderDetailID = orderDetail_ID_selected_from_browse_employees_page;

-- Update Order Details with input information
UPDATE OrderDetails
SET orderID = orderIDInput, productID = productIDInput
WHERE orderDetailID = orderDetail_ID_selected_from_browse_employees_page;

-- Update Orders
-- Get information for update on click of edit
SELECT orderID, orderDate, orderPrice,  Customers.customerName, Employees.employeeName 
FROM Orders
INNER JOIN Customers ON Orders.customerID = Customers.customerID 
INNER JOIN Employees ON Orders.employeeID = Employees.employeeID
WHERE orderID = order_ID_selected_from_browse_orders_page;

-- Update Order with input information
UPDATE Orders
SET orderID = :orderIDInput, orderDate = :orderDateInput, orderPrice = :orderPriceInput, customerID = :customer_id_from_dropdown_input, employeeID = :employee_id_from_dropdown_input
WHERE orderID = order_ID_selected_from_browse_orders_page;

--Update Product
-- Get information for update on click of edit
SELECT productID, productName, productDescription, productPrice, seasonSold 
FROM Products
WHERE productID = :product_ID_selected_from_browse_products_page; 

-- Update Product with input information
UPDATE Products 
SET productName = :productNameInput, productDescription = :productDescriptionInput, productPrice = :productPriceInput, seasonSold = :seasonSoldInput
WHERE productID = :product_ID_selected_from_browse_products_page;