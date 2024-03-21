# 0x00. MySQL advanced
## Learning Objectives
1) How to create tables with constraints 
2) How to optimize queries by adding indexes
3) What is and how to implement stored procedures and functions in MySQL
4) What is and how to implement views in MySQL
5) What is and how to implement triggers in MySQL

## Learning
We can learn about setting constraints during table creation from this basic syntax:
```
CREATE TABLE table_name (
  column1 data_type constraint_name,
  column2 data_type constraint_name,
  ...
  CONSTRAINT constraint_name table_constraint_definition
);
```
```table_name```: The name assigned to the table
```column1, column2```: Each column is associated to its data type (e.g. INT, VARCHAR, etc)
```constraint_name```: An optional name for the constraint
```table_constraint_definition```: This defines table-level constraints like primary key or foreign key

There are two main categories of constraints: column-level and table-level.
**Column level Constraints**
- NOT NULL
- UNIQUE
- DEFAULT
- CHECK

**Table level Constraints**
- PRIMARY KEY
- FOREIGN KEY

Let's consider the following table named Customers with constraints:
```
CREATE TABLE Customers (
  customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone_number CHAR(10) CHECK (LENGTH(phone_number) = 10)
);
```
In this example:
- ```customer_id```: is the primary key with auto-increment for unique identifiers
- ```name``` and ```email```: columns with the constraint, cannot be NULL
- ```phone_number```: column with the restriction of length 10 characters declared using the CHECK constraint

Let’s consider a table named Products in an e-commerce database. 
```
CREATE TABLE Products (
  product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(50) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL
);
```
Imagine a scenario where you frequently query to find all products in a specific category, like “Electronics”. Without an index, the database engine would need to scan every row in the Products table to find matching entries. This can be slow, especially for large tables. However by creating an index on the category column using the following statement:
```
CREATE INDEX idx_category ON Products(category)
```
When you query for products in a specific category, for instance:
```
SELECT * FROM Products WHERE category = 'Electronics';
```
The database engine can leverage on the index ```category```. Instead of scanning the entire table, it uses the index to quickly locate rows with “Electronics” in the category column.

In MySQL, stored procedures and functions are both ways of encapsulating a set of SQL statements for reusability and modularity. Here are some key differences between the two:
**Stored procedures**
- A block of SQL statements grouped under a specific name
- Can contain multiple SQL statements, including control flow (IF statements and Loops), and data manipulation statements (SELECT, INSERT, UPDATE, DELETE)
- Can return result sets directly to the client however it cannot return a single value

Here’s a basic example of a procedure:
**Creation**
```
-- Create a stored procedure to calculate product discount
CREATE PROCEDURE calculate_discount(IN price DECIMAL(10,2), IN discount_rate INT, OUT final_price DECIMAL(10,2))
BEGIN
  DECLARE discount DECIMAL(10,2);
  SET discount = price * discount_rate / 100;
  SET final_price = price - discount;
END;
```
**Usage**
```
-- Call the procedure to get the discounted price
CALL calculate_discount(100.00, 10, @final_price);
SELECT @final_price;  -- Display the discounted price
```

**Stored functions**
- A block of SQL statements that performs a specific task and returns a single value.
- Invoked directly within SQL expressions or other queries
- Cannot return result sets

Here is a basic example of a function:
**Creation**
```
-- Create a stored function to check product availability
CREATE FUNCTION is_available(IN product_id INT)
RETURNS TINYINT(1)
BEGIN
  DECLARE in_stock INT;
  SELECT stock INTO in_stock FROM Products WHERE product_id = product_id;
  RETURN IF(in_stock > 0, 1, 0);
END;
```
**Usage**
```
-- Use the function in a SELECT query
SELECT product_id, name, price, is_available(product_id) AS available
FROM Products;
```

A view in MySQL acts as a virtual table based on a pre-defined query. It doesn’t store data itself but presents a customized view of data from underlying tables. Views simply complex queries by hiding the underlying table structure and join operations from the user. Views can also pre-aggregate data, making it easier to perform calculations or summaries without writing complex joins every time.

Here is an example of creating a view named ```active_customers``` that shows customers with a positive balance from the ```Customers``` and ```Orders``` tables:
```
CREATE VIEW active_customers AS
SELECT c.customer_id, c.name, c.email
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Completed'
GROUP BY c.customer_id
HAVING SUM(o.amount) > 0;
```
Then, you can query the view just like a regular table:
```
SELECT * FROM active_customers;
```

Triggers are stored programs that automatically execute in response to specific events (INSERT, UPDATE, DELETE) on a particular table. They are useful for automating tasks or enforcing data integrity rules. There are two main categories of triggers: BEFORE vs AFTER and ROW-Level vs Statement-Level.

Here is an example of a trigger named ```update_stock``` that fires after a new order is inserted into the Orders table:
```
CREATE TRIGGER update_stock AFTER INSERT ON Orders
FOR EACH ROW
BEGIN
  UPDATE Products
  SET stock = stock - NEW.quantity
  WHERE product_id = NEW.product_id;
END;
```
This trigger automatically updates the product stock in the Products table whenever a new order is placed, subtracting the ordered quantity from the available stock for the corresponding product.
```

## Requirements
1) All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7
2) All your files should end with a new line
3) All your SQL queries should have a comment just before 
4) All your files should start with a comment describing the task
5) All SQL keywords should be in uppercase
6) A readme file, at the root of the folder of the project, is mandatory
7) The length of your flies will be tested using wc

## Use “container-on-demand” to run MySQL
- Ask for a container
- Connect via SSH or via the WebTerminal
- In the container, you should start MySQL before attempting the tasks
- The container credentials are root/root
```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```

## How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```


## Tasks
### 0. We are all unique!
Write a SQL script that creates a table users following these requirements:
With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
If the table already exists, your script should not fail
Your script can be executed on any database

### 1. In and not out
Write a SQL script that creates a table users following these requirements:
With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
If the table already exists, your script should not fail
Your script can be executed on any database

### 2. Best band ever!
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
Requirements:
Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ)
Column names must be: origin and nb_fans
Your script can be executed on any database

### 3. Old school band
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
Requirements:
Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ)
Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
You should use attributes formed and split for computing the lifespan
Your script can be executed on any database

### 4. Buy buy buy
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
Quantity in the table items can be negative.

### 5. Email validation to sent
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

### 6. Add bonus
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

### 7. Average score
Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student. Note: An average score can be a decimal

### 8. Optimize simple search
Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

### 9. Optimize search and score
Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

### 10. Safe divide
Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

### 11. No table for a meeting
Write an SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

### 12. Average weighted score
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student.

### 13. Average weighted score for all!
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.
