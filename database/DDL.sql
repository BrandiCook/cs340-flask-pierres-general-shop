    SET FOREIGN_KEY_CHECKS = 0;
    DROP TABLE IF EXISTS Orders;
    DROP TABLE IF EXISTS OrderDetails;
    DROP TABLE IF EXISTS Products;
    DROP TABLE IF EXISTS Customers; 
    DROP TABLE IF EXISTS Employees; 

    CREATE TABLE Employees (
        employeeID int(11) AUTO_INCREMENT NOT NULL,
        employeeName varchar(255) NOT NULL,
        employeeSalary int(11) NOT NULL, 
        PRIMARY KEY (employeeID), 
        CONSTRAINT employee_id_unique UNIQUE(employeeID)    
    );  

    CREATE TABLE Orders (
        orderID int(11) AUTO_INCREMENT NOT NULL,
        orderDate DATE NOT NULL,
        orderPrice int(11) NOT NULL,
        customerID int,
        employeeID int, 
        PRIMARY KEY (orderID),
        CONSTRAINT FOREIGN KEY (customerID) REFERENCES Customers(customerID) ON DELETE SET NULL,
        CONSTRAINT FOREIGN KEY (employeeID) REFERENCES Employees(employeeID) ON DELETE SET NULL
    );

    CREATE TABLE Customers (
    customerID INT(11) AUTO_INCREMENT NOT NULL,
    customerName VARCHAR(255) NOT NULL,
    dateOfBirth DATE NOT NULL,
    favoriteProduct INT(11),
    PRIMARY KEY (customerID),
    CONSTRAINT customer_id_unique UNIQUE(customerID), 
    CONSTRAINT FOREIGN KEY (favoriteProduct) REFERENCES Products(productID) ON DELETE SET NULL
    ); 

    CREATE TABLE OrderDetails (
        orderDetailID int(11) AUTO_INCREMENT NOT NULL,
        orderID int NOT NULL,
        productID int,
        PRIMARY KEY (orderDetailID),
        CONSTRAINT FOREIGN KEY (orderID) REFERENCES Orders(orderID) ON DELETE CASCADE,
        CONSTRAINT FOREIGN KEY (productID) REFERENCES Products(productID) ON DELETE SET NULL
    );

    CREATE TABLE Products (
        productID int(11) AUTO_INCREMENT NOT NULL,
        productName varchar(255) NOT NULL,
        productDescription varchar(255), 
        productPrice int(11) NOT NULL,
        seasonSold varchar(255) NOT NULL DEFAULT 'Year-Round',  
        PRIMARY KEY (productID),
        CONSTRAINT product_id_unique UNIQUE(productID)
    );

    INSERT INTO Employees (
        employeeName,
        employeeSalary
    )
    VALUES(
        'Pierre',
        250
    ),
    (
        'Abigail',
        150
    ),
    (
        'Caroline',
        150
    );

    INSERT INTO Orders (
        orderDate,
        orderPrice,
        customerID, 
        employeeID
    )
    VALUES 
    (
        '2022-02-07',
        500,
        1,
        1
    ),
    (
        '2022-02-10',
        300,
        2,
        2
    ),
    (
        '2022-03-01',
        550,
        3,
        3
    ),
    (
        '2022-03-07',
        1500,
        4,
        1
    ),
    (
        '2022-03-15',
        20,
        2,
        1
    );

    INSERT INTO OrderDetails (
        orderID,
        productID
    )
    VALUES 
    (
        1,
        3
    ),
    (
        2,
        4
    ),
    (
        3,
        5
    );

    INSERT INTO Products (
        productName,
        productDescription,
        productPrice,
        seasonSold
    )
    VALUES 
    (
        'Grass Starter',
        'Place this on your farm to start a new patch of grass.',
        100,
        "Year-Round"
    ),
    (
        'Sugar',
        'Adds sweetness to pastries and candies. Too much can be unhealthy.',
        100,
        "Year-Round"
    ),
    (
        'Wheat Flour',
        'A common cooking ingredient made from crushed wheat seeds.',
        100,
        "Year-Round"
    ),
    (
        'Rice',
        'A basic grain often served under vegetables.',
        200,
        "Year-Round"
    ),
    (
        'Bouquet',
        'A gift that shows your romantic interest.',
        200,
        "Year-Round"
    ),
    (
        'Parsnip Seeds',
        'Plant these in the spring. Takes 4 days to mature.',
        20,
        "Spring"
    ),
    (
        'Bean Starter',
        'Plant these in the spring. Takes 10 days to mature, but keeps producing after that. Grows on a trellis.', 
        60,
        "Spring"
    ),
    (
        'Cauliflower Seeds',
        'Plant these in the spring. Takes 12 days to produce a large cauliflower.', 
        80,
        "Spring"
    ),
    (
        'Melon Seeds',
        'Plant these in the summer. Takes 12 days to mature.', 
        80,
        "Summer"
    ),
    (
        'Tomato Seeds',
        'Plant these in the summer. Takes 11 days to mature, and continues to produce after first harvest.', 
        50,
        "Summer"
    ),
    (
        'Blueberry Seeds',
        'Plant these in the summer. Takes 13 days to mature, and continues to produce after first harvest.', 
        80,
        "Summer"
    ),
    (
        'Eggplant Seeds',
        'Plant these in the fall. Takes 5 days to mature, and continues to produce after first harvest.', 
        20,
        "Fall"
    ),
    (
        'Corn Seeds',
        'Plant these in the summer or fall. Takes 14 days to mature, and continues to produce after first harvest.', 
        150,
        "Fall"
    ),
    (
        'Pumpkin Seeds',
        'Plant these in the fall. Takes 13 days to mature.', 
        100,
        "Fall"
    ); 

    INSERT INTO Customers ( 
        customerName, 
        dateOfBirth, 
        favoriteProduct 
    )
    VALUES
    ('Pam', '1979-05-18', 1),
    ('Shane', '1995-04-20', 3),
    ('George', '1962-10-24', 2),
    ('Jodi', '1988-09-11', 3),
    ('Wizard', '1900-12-17', 4);

    SET FOREIGN_KEY_CHECKS=1;
    COMMIT;
