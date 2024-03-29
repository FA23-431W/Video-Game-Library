from util import *
from datetime import datetime


def convert_to_datetime(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y')


def sort_games(games_list):
    """
    Sort a list of games based on user-selected criteria.

    :param games_list: List of games, each game is a tuple (gameID, Title, mainCate, price, release)
    :return: Sorted list of games
    """
    print("\n--- Sort Games ---")
    print("\n--- Sort Games ---")
    print("1. Sort by Name")
    print("2. Sort by Price")
    print("3. Sort by Date")

    choice = input("Choose your sorting criteria: ")

    if choice == "1":
        # Sort by Title (name)
        sorted_games = sorted(games_list, key=lambda x: x[1].lower())  # x[1] is the Title
    elif choice == "2":
        # Sort by Price
        sorted_games = sorted(games_list, key=lambda x: float(x[3]))  # x[3] is the Price
    elif choice == "3":
        # Sort by Release Date
        sorted_games = sorted(games_list, key=lambda x: convert_to_datetime(x[4]))
    else:
        print("Invalid choice. Please try again.")
        return games_list

    return sorted_games

    pass


def show_gamelist(conn, game_list, user_id):
    """
       This function receive a list of games in the format of
       gameID | Title | mainCate | price | release 

       and do the following thing:
       - display them on terminal 
       - Provide sort options
       - View certain Game's info
       
     """

    while True:
        display_game_list(game_list)  # Display games in selected category

        print("\n--- Game Library Options ---")
        print("1. Sort By")
        print("2. View Certain Game")
        print("3. Add Game to wishlist")
        print("4. Return to Game Library Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            game_list = sort_games(game_list)  # Implement this to sort games
        elif choice == "2":
            game_id = input("Enter Game ID to view details: ")
            see_game_details(conn, game_id, user_id)  # Use the already implemented function
        elif choice == "3":
            game_id = input("Enter Game ID to add into wishlist: ")
            add_wishlist(conn, game_id, user_id)
        elif choice == "4":
            break  # Return to the previous menu
        else:
            print("Invalid choice. Please try again.")


def get_games_from_cata(conn, category):
    try:
        cur = conn.cursor()
        query = "SELECT gameID, Title, mainCate, price, `release` FROM Game WHERE mainCate = %s"
        cur.execute(query, (category,))
        games = cur.fetchall()

        if games:
            return games
        else:
            print(f"No games found in {category} category.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")


def get_categories(conn):
    """
    Fetch all unique game categories.

    :param conn: Database connection object
    :return: List of categorie
    """
    categories = []
    try:
        cur = conn.cursor()
        query = "SELECT DISTINCT mainCate FROM Game ORDER BY mainCate"
        cur.execute(query)
        categories = [category[0] for category in cur.fetchall()]
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")

    return categories


def get_all_games(conn):
    """
    Fetch all games from the database.

    :param conn: Database connection object
    :return: List of all games
    """
    try:
        # Create a new cursor
        cur = conn.cursor()

        # SQL query to select all games
        query = "SELECT gameID, Title, mainCate, price, `release` FROM Game"

        # Execute the query
        cur.execute(query)

        # Fetch all the results
        game_list = cur.fetchall()

        # Return the list of games
        return game_list

    except mysql.connector.Error as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {e}")

    return []  # Return an empty list if an error occurs or no games are found


def browse_by_category(conn, user_id):
    categories = get_categories(conn)  # Fetch categories

    if categories:
        print("\nAvailable Categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")

        try:
            choice = int(input("\nEnter the number of the category to browse: ")) - 1
            if 0 <= choice < len(categories):
                game_list = get_games_from_cata(conn, categories[choice])
                show_gamelist(conn, game_list, user_id)

            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No categories found.")


def show_all_games(conn, user_id):
    print("\nAll Games:")
    game_list = get_all_games(conn)

    while True:
        display_game_list(game_list)
        print("\n1. Sort Games")
        print("2. View Certain Game")
        print("3. Add Game to wishlist")
        print("4. Return")

        choice = input("Enter your choice: ")

        if choice == "1":
            game_list = sort_games(game_list)  # Implement this to sort games
        elif choice == "2":
            game_id = input("Enter Game ID to view details: ")
            see_game_details(conn, game_id, user_id)
        elif choice == '3':
            game_id = input("Enter Game ID to add into wishlist: ")
            add_wishlist(conn, game_id, user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def game_library_menu(conn, user_id):
    while True:
        print("\n--- Game Library Menu ---")
        print("1. Browse by Category")
        print("2. Show All Games")
        print("3. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            browse_by_category(conn, user_id)
        elif choice == "2":
            show_all_games(conn, user_id)
        elif choice == "3":
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = create_connection()
    if conn:
        game_library_menu(conn, 977)
        conn.close()
    else:
        print("Failed to establish a database connection.")
