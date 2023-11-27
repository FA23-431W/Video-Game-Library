import sqlite3


def login(conn, name, password):
    """
    Login function to authenticate a user.
    :param conn: Database connection object
    :param username: The username of the user
    :param password: The password of the user
    :return: True if login is successful, False otherwise
    """
    cur = conn.cursor()

    try:
        # Prepare a query to select the user
        query = "SELECT * FROM User WHERE name=? AND password=?"
        cur.execute(query, (name, password))

        # Fetch one record, if user exists
        user = cur.fetchone()
        if user:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
def user_menu():

    pass