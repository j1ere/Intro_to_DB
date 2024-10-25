import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Database connection details (replace with your MySQL credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="jeremiah",
            password=""
        )
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Database connection failed: {err}")
    
    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        print("Database connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()
