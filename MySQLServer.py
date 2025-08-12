# MySQLServer.py
import mysql.connector
from mysql.connector import Error
import sys # Import sys for flushing output

print("Script started. Initializing database creation process...")
sys.stdout.flush() # Ensure this print is displayed immediately

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
        print("Attempting to connect to MySQL server...")
        sys.stdout.flush() # Ensure this print is displayed immediately

        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Nahom@8665"
        )

        print("Connection attempt completed.")
        sys.stdout.flush() # Ensure this print is displayed immediately

        if connection.is_connected():
            print("Successfully connected to MySQL server.")
            sys.stdout.flush() # Ensure this print is displayed immediately
            cursor = connection.cursor()

            create_db_query = f"CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            print(f"Database '{db_name}' created successfully!")
            sys.stdout.flush() # Ensure this print is displayed immediately
        else:
            print("Failed to connect to MySQL server (connection not established).")
            sys.stdout.flush() # Ensure this print is displayed immediately

    except Exception as e: # <--- CHANGED FROM 'Error' to 'Exception'
        print(f"An unexpected error occurred: {e}")
        sys.stdout.flush() # Ensure this print is displayed immediately
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed.")
            sys.stdout.flush() # Ensure this print is displayed immediately
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")
            sys.stdout.flush() # Ensure this print is displayed immediately
        elif connection: # If connection object exists but isn't connected (e.g. failed to connect)
            print("Connection object existed but was not connected (or failed to connect fully).")
            sys.stdout.flush() # Ensure this print is displayed immediately


if __name__ == "__main__":
    create_alx_book_store_db()