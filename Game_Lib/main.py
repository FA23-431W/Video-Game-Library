from user import user_menu
from admin import admin_menu
from util import *

def login(conn, username, password):
    username = "ggallager1"
    password = 'vF9=Qm"lJG'

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
        query = "SELECT userID FROM User WHERE name=%s AND password=%s"
        cur.execute(query, (username, password))
        # Fetch one record
        user = cur.fetchone()
        if user:
            return user[0]  # Return the userID
        else:
            return None
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        return None




# Update your main_menu function to use the MySQL connection
def main_menu(conn):
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
                # !! this is a temp, after implementing admin functionality, use adminid to check
                if name == "admin":
                    admin_menu(conn, user_id)
                    pass
                else:
                    user_menu(conn, user_id)
            else:
                print("Login failed, No such user & password. Please try again.")
        elif choice == "2":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = create_connection()
    if conn:
        main_menu(conn)
        conn.close()
    else:
        print("Failed to establish a database connection.")
