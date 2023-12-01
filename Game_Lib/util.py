import sqlite3
import mysql.connector

def display_game_list(game_info):
    if game_info:
        header = "{:<8} | {:<40} | {:<15} | {:<10} | {:<15}"
        print(header.format("Game ID", "Title", "Category", "Price", "Release Date"))
        print("-" * 100)

        for item in game_info:
            print(header.format(item[0], item[1], item[2], item[3], item[4]))
    else:
        print("Your wishlist is empty.")


def create_connection():
    """Create a database connection to the MySQL server."""
    try:
        conn = mysql.connector.connect(
            host='localhost',  # Your MySQL server host
            user='root',  # Your MySQL username
            password='291878113',  # Your MySQL password
            database='Game_Lib'  # Your database name
        )
        return conn
    except mysql.connector.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None


# This function leads user to the community page,
# where user can browse the review under certain game
# and also add comments to the dashborad

def fetch_posts(conn, game_id):
    """
    Fetch and display dashboard posts for a specific game.

    :param conn: Database connection object
    :param game_id: The ID of the game
    """

    # TYPO in Community!
    try:
        cur = conn.cursor()
        query = """
        SELECT d.post, d.date, d.Author
        FROM Dashboard d
        JOIN Community c ON d.dashboardID = c.dashboardID
        WHERE c.gameID = %s
        ORDER BY d.date DESC
        """
        cur.execute(query, (game_id,))
        posts = cur.fetchall()

        if posts:
            print("\n--- Game Community Dashboard ---")
            for post in posts:
                print(f"Date: {post[1]}, Author: {post[2]}\nPost: {post[0]}\n")
        else:
            print("No posts found for this game.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")


def add_comment_to_dashboard(conn, game_id, user_id):
    """
    Allow the user to add a comment to the dashboard for a specific game.

    :param conn: Database connection object
    :param game_id: The ID of the game
    :param user_id: The ID of the user
    """
    try:
        # Fetch the dashboardID for this game
        cur = conn.cursor()
        query = "SELECT dashboardID FROM Community WHERE gameID = %s"
        cur.execute(query, (game_id,))
        result = cur.fetchone()

        if result:
            dashboard_id = result[0]

            post = input("Enter your comment: ")
            date = "CURRENT_DATE"  # Replace with your date handling as needed
            author = user_id  # Replace with actual author identifier

            # Insert the new comment
            insert_query = """
            INSERT INTO Dashboard (dashboardID, post, date, Author)
            VALUES (%s, %s, %s, %s)
            """
            cur.execute(insert_query, (dashboard_id, post, date, author))
            conn.commit()
            print("Your comment has been added.")

        else:
            print("No dashboard found for this game.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback any changes if there's an error


def goto_community(conn, game_id, user_id):
    """
    Lead user to the community page for a specific game.

    :param conn: Database connection object
    :param game_id: The ID of the game
    :param user_id: The ID of the user
    """
    fetch_posts(conn, game_id)  # Display existing posts

    while True:
        print("\nCommunity Options:")
        print("1. Add Comment")
        print("2. Return to Game Library")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_comment_to_dashboard(conn, game_id, user_id)  # Implement this function
        elif choice == "2":
            break  # Return to the previous menu
        else:
            print("Invalid choice. Please try again.")


def see_game_details(conn, game_id, user_id):
    """
    Display details of a certain game, including the number of users who added it to their wishlist.
    The user should be able to access the game's community or return to the previous page.

    :param conn: Database connection object
    :param game_id: The ID of the game to view details
    """
    try:
        cur = conn.cursor()

        # SQL query to fetch game details and the count of users who added the game to their wishlist
        query = """
        SELECT g.gameID, g.Title, p.name, g.mainCate, g.price, g.release, COUNT(wg.gameID)
        FROM Game g
        LEFT JOIN Publisher p ON g.publisherID = p.publisherID
        LEFT JOIN WishlistGame wg ON g.gameID = wg.gameID
        WHERE g.gameID = %s
        GROUP BY g.gameID
        """

        cur.execute(query, (game_id,))
        game_details = cur.fetchone()

        if game_details:
            while True:
                print("\n********** Game Details **********")
                print(f"Game ID        : {game_details[0]}")
                print(f"Title          : {game_details[1]}")
                print(f"Publisher      : {game_details[2]}")
                print(f"Category       : {game_details[3]}")
                print(f"Price          : ${game_details[4]:.2f}")  # Assuming price is a float
                print(f"Release Date   : {game_details[5]}")
                print(f"Users Interested: {game_details[6]}")
                print("**********************************\n")

                print("1. Go to Community")
                print("2. Return to User Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    # Go to Community
                    goto_community(conn, game_id, user_id)
                elif choice == "2":
                    break  # Return to the previous menu
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Game not found.")
            input("\nEnter any input to return...")  # Wait for user input

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
