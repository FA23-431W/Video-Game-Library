from util import *


def remove_game_from_wishlist(conn, user_id, game_id):
    try:
        cur = conn.cursor()

        # Check if the game is in the user's wishlist
        cur.execute("""
            SELECT * FROM WishlistGame
            WHERE wishlistID = (
                SELECT wishlistID FROM WishlistUser WHERE userID = %s
            ) AND gameID = %s
        """, (user_id, game_id))
        if not cur.fetchone():
            print(f"Game with ID {game_id} is not in the user's wishlist.")
            return

        # Step 1: Remove the game from the WishlistGame table
        delete_query = """
            DELETE FROM WishlistGame
            WHERE wishlistID = (
                SELECT wishlistID FROM WishlistUser WHERE userID = %s
            ) AND gameID = %s
        """
        cur.execute(delete_query, (user_id, game_id))

        # Step 2: Check if the wishlist is now empty, and update the User table if necessary
        check_query = """
            SELECT COUNT(*) FROM WishlistGame
            WHERE wishlistID = (
                SELECT wishlistID FROM WishlistUser WHERE userID = %s
            )
        """
        cur.execute(check_query, (user_id,))
        count = cur.fetchone()[0]

        if count == 0:
            # If the wishlist is empty, update the User table
            update_query = "UPDATE User SET wishlistID = NULL WHERE userID = %s"
            cur.execute(update_query, (user_id,))

        conn.commit()
        print(f"Game with ID {game_id} has been removed from the user's wishlist.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback in case of error


def wishlist_menu(conn, user_id):
    while True:
        print("\n###################### My Wishlist  ######################")

        # get all games and their info in this user's wishlist
        query = """
            SELECT g.gameID, g.Title, g.mainCate, g.price, g.release
            FROM User u
            JOIN WishlistUser wu ON u.userID = wu.userID
            JOIN WishlistGame wg ON wu.wishlistID = wg.wishlistID
            JOIN Game g ON wg.gameID = g.gameID
            WHERE u.userID = %s;
               """
        cur = conn.cursor()
        cur.execute(query, (user_id,))  # Pass the wishlist_id to the query
        game_list = cur.fetchall()

        if game_list:
            display_game_list(game_list)
        else:
            print("No games found in this wishlist.")
            break

        print("\n1. See Game Details")
        print("2. Remove Game from Wishlist")
        print("3. Return to Wishlist Menu")
        print("###################### My Wishlist  ######################")

        choice = input("Enter your choice: ")

        # Option 1
        if choice == "1":
            game_id = input("Enter Game ID to view details: ")
            see_game_details(conn, game_id, user_id)
        # Option 2
        elif choice == "2":
            game_id = input("Enter game ID to remove from wishlist: ")
            remove_game_from_wishlist(conn, user_id, game_id)  # Implement this function
        # Option 3
        elif choice == "3":
            break  # Exit the wishlist menu
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = create_connection()
    if conn:
        wishlist_menu(conn, 977)
        conn.close()
    else:
        print("Failed to establish a database connection.")
