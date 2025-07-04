
# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_alx_book_store_db():
    """
    Connects to MySQL server and creates the 'alx_book_store' database
    if it does not already exist. Handles connection errors and closes
    the connection properly.
    """
    db_name = "alx_book_store"
    connection = None
    cursor = None

    try:
        # Establish a connection to the MySQL server
        # You might need to change host, user, and password based on your MySQL setup
        connection = mysql.connector.connect(
            host="localhost",  # Or your MySQL server's IP address/hostname
            user="root",       # Your MySQL username
            password="your_mysql_password" # Your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to create the database if it doesn't exist
            # Using IF NOT EXISTS ensures the script does not fail if the DB already exists
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
            cursor.execute(create_db_query)

            print(f"Database '{db_name}' created successfully!")
        else:
            print("Failed to connect to MySQL server.")

    except Error as e:
        # Handle specific MySQL connection errors
        print(f"Error connecting to MySQL or creating database: {e}")
    finally:
        # Ensure cursor and connection are closed properly
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    # --- IMPORTANT ---
    # Replace 'your_mysql_password' with your actual MySQL root password
    # before running the script.
    # ---
    create_alx_book_store_db()