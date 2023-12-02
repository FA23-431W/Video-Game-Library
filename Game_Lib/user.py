import sqlite3
from game_lib import *
from wishlist import *
from util import *




def user_menu(conn, user_id):
    while True:
        print("\n----------- User Menu -----------")
        print("1. See My Wishlist")
        print("2. Game Library")
        print("3. Logout")
        print("----------- User Menu ------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            wishlist_menu(conn, user_id)
        elif choice == "2":
            game_library_menu(conn, user_id)
        elif choice == "3":
            print("Logout")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    if __name__ == '__main__':
        conn = create_connection()
        if conn:
            user_menu(conn)
            conn.close()
        else:
            print("Failed to establish a database connection.")
