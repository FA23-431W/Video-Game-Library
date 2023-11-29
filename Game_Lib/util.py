import sqlite3


def display_game_list(game_info):
    if game_info:
        print("\nYour Wishlist Games:")
        header = "{:<8} | {:<40} | {:<15} | {:<10} | {:<15}"
        print(header.format("Game ID", "Title", "Category", "Price", "Release Date"))
        print("-" * 100)

        for item in game_info:
            print(header.format(item[0], item[1], item[2], item[3], item[4]))
    else:
        print("Your wishlist is empty.")


def goto_community():
    pass


def see_game_details(conn, game_id):
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
        WHERE g.gameID = ?
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
                    goto_community()  # Implement this function to handle community interactions
                elif choice == "2":
                    break  # Return to the previous menu
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Game not found.")
            input("\nEnter any input to return...")  # Wait for user input

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
