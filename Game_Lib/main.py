import sqlite3
import user

from user import *
from admin import *


def login(conn, username, password):
    """
    Login function to authenticate a user and return their userID.

    :param conn: Database connection object
    :param username: The username of the user
    :param password: The password of the user
    :return: userID if login is successful, None otherwise
    """
    cur = conn.cursor()

    try:
        # Query to check if user exists and fetch their userID
        query = "SELECT userID FROM User WHERE name=? AND password=?"
        cur.execute(query, (username, password))
        # Fetch one record
        user = cur.fetchone()
        if user:
            return user[0]  # Return the userID
        else:
            return None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def main_menu():
    while True:
        print("    Welcome to the Game Library App !")
        print("------------------------------------------")
        print("1. Login")
        print("2. Exit")
        print("------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter username: \n")
            password = input("Enter password: ")
            user_id = login(conn, name, password)  # Now login returns userID

            if user_id is not None:
                print("Login successful!\n")
                print("Welcome {} ! \nUser ID: {}".format(name, user_id))
                # Check if the user is admin
                # !! this is a temp, after implement admin, we should use adminid to check
                if name == "admin":
                    admin_menu(conn, user_id)
                else:
                    user_menu(conn, user_id)
            else:
                print("Login failed, No such user & passward. Please try again.")
        elif choice == "2":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = create_connection("Data/data.db")
    main_menu()
    conn.close()
