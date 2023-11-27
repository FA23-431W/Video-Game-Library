import sqlite3

import user
from user import *
from admin import *


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def main_menu():
    # the main menu
    # Call appropriate functions based on user input
    while True:
        print("Welcome to the Game Directory App")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter username: ")
            password = input("Enter password: ")
            if login(conn, name, password):
                print("Login successful!")
                # Proceed to user menu
                if name == "admin":
                    admin_menu()
                else:
                    user_menu()
            else:
                print("Login failed. Please try again.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
    pass


if __name__ == '__main__':
    conn = create_connection("Data/data.db")
    main_menu()
    conn.close()
