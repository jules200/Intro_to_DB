import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

# SQL statements
CREATE_DATABASE = "CREATE DATABASE IF NOT EXISTS alx_book_store"
USE_DATABASE = "USE alx_book_store"

CREATE_AUTHORS_TABLE = """
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
)
"""

CREATE_BOOKS_TABLE = """
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
)
"""

CREATE_CUSTOMERS_TABLE = """
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
)
"""

CREATE_ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
"""

CREATE_ORDER_DETAILS_TABLE = """
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
)
"""

# Function to create and initialize the database
def create_database_and_tables(cursor):
    try:
        cursor.execute(CREATE_DATABASE)
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        return
    
    cursor.execute(USE_DATABASE)
    
    cursor.execute(CREATE_AUTHORS_TABLE)
    cursor.execute(CREATE_BOOKS_TABLE)
    cursor.execute(CREATE_CUSTOMERS_TABLE)
    cursor.execute(CREATE_ORDERS_TABLE)
    cursor.execute(CREATE_ORDER_DETAILS_TABLE)
    print("Tables created successfully!")

# Main script execution
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    
    create_database_and_tables(cursor)
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()
    print("Database connection closed.")