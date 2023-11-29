import sqlite3
from util import *


def sort_games(games_list):
    """
    Sort a list of games based on user-selected criteria.

    :param games_list: List of games, each game is a tuple (gameID, Title, mainCate, price, release)
    :return: Sorted list of games
    """
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
        sorted_games = sorted(games_list, key=lambda x: x[4])  # x[4] is the Release Date
    else:
        print("Invalid choice. Please try again.")
        return games_list

    return sorted_games


    pass


def show_gamelist(game_list):
    display_game_list(game_list)  # Display games in selected category
    """
       This function receive a list of games in the format of
       gameID | Title | mainCate | price | release 

       and do the following thing:
       - display them on terminal 
       - Provide sort options
       - View certain Game's info
       
     """

    while True:
        print("\n--- Game Library Options ---")
        print("1. Sort By")
        print("2. View Certain Game")
        print("3. Return to Game Library Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            games = sort_games(game_list)  # Implement this to sort games
        elif choice == "2":
            game_id = input("Enter Game ID to view details: ")
            see_game_details(conn, game_id)  # Use the already implemented function
        elif choice == "3":
            break  # Return to the previous menu
        else:
            print("Invalid choice. Please try again.")

        # Re-display the sorted/updated list of games
        if choice == "1":
            display_game_list(games)  # Implement this to display the list of games


def get_games_from_cata(category):
    try:
        cur = conn.cursor()
        query = "SELECT gameID, Title, mainCate, price, release FROM Game WHERE mainCate = ?"
        cur.execute(query, (category,))
        games = cur.fetchall()

        if games:
            return games
        else:
            print(f"No games found in {category} category.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def get_categories(conn):
    """
    Fetch all unique game categories.

    :param conn: Database connection object
    :return: List of categories
    """
    categories = []
    try:
        cur = conn.cursor()
        query = "SELECT DISTINCT mainCate FROM Game ORDER BY mainCate"
        cur.execute(query)
        categories = [category[0] for category in cur.fetchall()]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    return categories


def game_lib_options(conn, games):
    pass


def browse_by_category(conn):
    categories = get_categories(conn)  # Fetch categories

    if categories:
        print("\nAvailable Categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")

        try:
            choice = int(input("\nEnter the number of the category to browse: ")) - 1
            if 0 <= choice < len(categories):
                game_list = get_games_from_cata(categories[choice])
                show_gamelist(game_list)

            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No categories found.")


def get_all_games(conn):
    pass


def show_all_games(conn):
    print("\nAll Games:")
    games = display_game_list(conn)  # Implement this to fetch and show all games

    while True:
        print("\n1. Sort Games")
        print("2. View Certain Game")
        print("3. Return")

        choice = input("Enter your choice: ")

        if choice == "1":
            sort_games(games)  # Implement this to sort games
        elif choice == "2":
            game_id = input("Enter Game ID to view details: ")
            see_game_details(conn, game_id)
        elif choice == "3":
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
            browse_by_category(conn)
        elif choice == "2":
            show_all_games(conn)
        elif choice == "3":
            break  # Return to the main menu
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = sqlite3.connect("Data/data.db")
    game_library_menu(conn, 997)
