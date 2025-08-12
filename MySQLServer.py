# MySQLServer.py
import mysql.connector
from mysql.connector import Error
import sys

def create_alx_book_store_db():
    """
    Connects to MySQL server and creates the 'alx_book_store' database
    if it does not already exist.
    """
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            
            print("Database 'alx_book_store' created successfully!")
            sys.stdout.flush()

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.stdout.flush()
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")
            sys.stdout.flush()

if __name__ == "__main__":
    create_alx_book_store_db()