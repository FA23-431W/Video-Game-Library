# import sqlite3
import mysql.connector
from datetime import datetime


def add_wishlist(conn, game_id, user_id):
    try:
        cur = conn.cursor()

        # Step 1: Insert into WishlistUser (if not already there)
        cur.execute("SELECT wishlistID FROM WishlistUser WHERE userID = %s", (user_id,))
        result = cur.fetchone()
        if not result:
            # Create new WishlistUser entry
            cur.execute("INSERT INTO WishlistUser (userID) VALUES (%s)", (user_id,))
            wishlist_id = cur.lastrowid
        else:
            wishlist_id = result[0]

        # Step 2: Check if the game is already in the wishlist
        cur.execute("SELECT * FROM WishlistGame WHERE wishlistID = %s AND gameID = %s", (wishlist_id, game_id))
        if cur.fetchone():
            print("Game already in wishlist.")
            return

        # Step 3: Insert the game into the WishlistGame
        cur.execute("INSERT INTO WishlistGame (wishlistID, gameID) VALUES (%s, %s)", (wishlist_id, game_id))
        conn.commit()
        print("Game added to wishlist successfully.")
        input("Press Any Key to Return")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()





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

        # SQL query updated to order by date in ascending order
        query = """
        SELECT d.post, d.date, d.Author
        FROM Dashboard d
        JOIN Community c ON d.communityID = c.communityID
        WHERE c.gameID = %s
        ORDER BY d.date ASC  -- Order by date in ascending order
        """

        cur.execute(query, (game_id,))
        posts = cur.fetchall()
        cur.close()

        if posts:
            print("\n--- Community Posts ---")
            for post in posts:
                # Enhanced formatting for the output
                print(f"Date: {post[1]} | Author: {post[2]}")
                print(f"Post: {post[0]}")
                print("-" * 50)
        else:
            print("No posts found for this game.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")

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

    try:
        cur = conn.cursor()

        # SQL query to fetch game details
        query = """
        SELECT g.gameID, g.Title, p.name, g.mainCate, g.price, g.release
        FROM Game g
        LEFT JOIN Publisher p ON g.publisherID = p.publisherID
        WHERE g.gameID = %s
        """
        cur.execute(query, (game_id,))
        game_details = cur.fetchone()

        # Query to count the number of users who added the game to their wishlist
        wishlist_count_query = """
        SELECT COUNT(*) FROM WishlistGame WHERE gameID = %s
        """
        cur.execute(wishlist_count_query, (game_id,))
        wishlist_count = cur.fetchone()[0]

        # Query to count the number of posts in the game's community
        posts_count_query = """
        SELECT COUNT(*) FROM Dashboard WHERE communityID IN 
        (SELECT communityID FROM Community WHERE gameID = %s)
        """
        cur.execute(posts_count_query, (game_id,))
        posts_count = cur.fetchone()[0]

        cur.close()

        if game_details:
            while True:
                print("\n********** Game Details **********")
                print(f"Game ID        : {game_details[0]}")
                print(f"Title          : {game_details[1]}")
                print(f"Publisher      : {game_details[2]}")
                print(f"Category       : {game_details[3]}")
                print(f"Price          : ${game_details[4]:.2f}")  # Assuming price is a float
                print(f"Release Date   : {game_details[5]}")
                print(f"Users Interested: {wishlist_count}")
                print(f"Community Posts: {posts_count}")
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
        if cur is not None:
            cur.close()  # Ensure the cursor is closed

