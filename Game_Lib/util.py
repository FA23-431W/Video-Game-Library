# import sqlite3
import mysql.connector
from datetime import datetime


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
    try:
        cur = conn.cursor(buffered=True)

        # Updated SQL query
        query = """
        SELECT d.post, d.date, d.Author
        FROM Dashboard d
        JOIN Community c ON d.communityID = c.communityID
        WHERE c.gameID = %s
        ORDER BY d.date DESC
        """

        cur.execute(query, (game_id,))
        posts = cur.fetchall()
        cur.close()
        if posts:
            print("\n--- Community Posts ---")
            for post in posts:
                print(f"Date: {post[1]}, Author: {post[2]}")
                print(post[0])
                print("-" * 50)
        else:
            print("No posts found for this game.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()  # Close the cursor in the finally block

import mysql.connector
from datetime import datetime

import mysql.connector
from datetime import datetime


def add_comment_to_dashboard(conn, game_id, author_name):
    try:
        with conn.cursor() as cur:
            # Check for existing community for the game
            cur.execute("SELECT communityID FROM Community WHERE gameID = %s", (game_id,))
            community_result = cur.fetchone()

            # If no community exists, create one
            if not community_result:
                cur.execute("INSERT INTO Community (gameID) VALUES (%s)", (game_id,))
                conn.commit()  # Commit the new community creation
                community_id = cur.lastrowid  # Get the new community ID
            else:
                community_id = community_result[0]

            # Prompt for user comment
            post = input("Enter your comment: ")
            date = datetime.now().strftime("%Y-%m-%d")

            # Add the comment to the Dashboard
            cur.execute("INSERT INTO Dashboard (post, date, Author, communityID) VALUES (%s, %s, %s, %s)",
                        (post, date, author_name, community_id))
            conn.commit()
            print("Your comment has been added.")
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()



def goto_community(conn, game_id, user_id):
    """
    Lead user to the community page for a specific game.

    :param conn: Database connection object
    :param game_id: The ID of the game
    :param user_id: The ID of the user
    """

    while True:
        fetch_posts(conn, game_id)  # Display existing posts
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
        cur.close

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
    finally:
        cur.close()  # Close the cursor in the finally block