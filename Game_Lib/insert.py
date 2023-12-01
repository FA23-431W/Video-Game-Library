import sqlite3
# from admin import admin_menu

def insert_menu(conn, user_id):
  while True:
    print("\n----------- Insert Menu -----------")
    print("1. Insert game")
    print("2. Insert publisher")
    print("3. Insert Achievement")
    print("4. Insert category")
    print("5. Insert community")
    print("6. Return")
    print("----------- Insert Menu ------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        insert_game(conn)
    elif choice == "2":
        insert_publisher(conn)
    elif choice == "3":
        insert_achievemnt(conn)
    elif choice == "4":
        insert_category(conn)
    elif choice == "5":
        insert_community(conn)
    elif choice == "6":
        # admin_menu(conn, user_id)
        break
    else:
        print("Invalid choice. Please try again.")
      
def insert_game(conn):
  """
  Allow the admin to add game to the library.

  :param conn: Database connection object
  """
  try:
      cur = conn.cursor()
  
      gameID = input("Enter new gameID: ")
      publisherID = input("Enter the new game's publisherID: ")
      title = input("Enter the new game's title: ")
      mainCate = input("Enter the new game's main category: ")
      price = input("Enter the new game's price: ")
      release = input("Enter the release date time of the new game: ")
      # Insert the new game
      insert_query = """
          INSERT INTO Game(publisherID, gameID, title, mainCate, price, release)
          VALUES (?, ?, ?, ?, ?, ?)
          """
      cur.execute(insert_query, (publisherID,gameID,title,mainCate,price,release))
      conn.commit()
      print("Your game has been added.")


  except sqlite3.Error as e:
      print(f"An error occurred: {e}")
      conn.rollback()  

def insert_publisher(conn):
  """
  Allow the admin to add new publisher to the library.

  :param conn: Database connection object
  """
  try:
      cur = conn.cursor()

      publisherID = input("Enter the new publisher's ID: ")
      name = input("Enter the new publisher's name: ")
      year = input("Enter the new publisher's release year: ")

      # Insert the new publisher
      insert_query = """
          INSERT INTO Publisher(publisherID, name, year))
          VALUES (?, ?, ?)
          """
      cur.execute(insert_query, (publisherID,name,year))
      conn.commit()
      print("Your new publisher has been added.")


  except sqlite3.Error as e:
      print(f"An error occurred: {e}")
      conn.rollback()  

def insert_achievemnt(conn):
  """
  Allow the admin to add new achievement of certain game to the library.

  :param conn: Database connection object
  """
  try:
      cur = conn.cursor()

      achievementID = input("Enter the new achievemntID: ")
      description = input("Enter the new achievement's description: ")
      gameID = input("Enter the new achievement's according gameID: ")

      # Insert the new achievement
      insert_query = """
          INSERT INTO Achievement(achievementID, description, gameID))
          VALUES (?, ?, ?)
          """
      cur.execute(insert_query, (achievementID,description,gameID))
      conn.commit()
      print("Your new achievemnt has been added.")


  except sqlite3.Error as e:
      print(f"An error occurred: {e}")
      conn.rollback() 

def insert_category(conn):
  """
  Allow the admin to add new sub category according to the main category to the library.

  :param conn: Database connection object
  """
  try:
      cur = conn.cursor()

      subCate = input("Enter the new subcategory of the main category: ")
      mainCate = input("Enter the main category that relates to the sub category: ")

      # Insert the new subcategory
      insert_query = """
          INSERT INTO Category(subCate, mainCate))
          VALUES (?, ?)
          """
      cur.execute(insert_query, (subCate, mainCate))
      conn.commit()
      print("Your new subcategory has been added.")


  except sqlite3.Error as e:
      print(f"An error occurred: {e}")
      conn.rollback() 


def insert_community(conn):
  """
  Allow the admin to add new community to the library.

  :param conn: Database connection object
  """
  try:
      cur = conn.cursor()

      gameID = input("Enter the gameID that is related to the new community: ")
      communityID = input("Enter the new communityID: ")
      dashboardID = input("Enter the new communityID's dashboardID: ")

      # Insert the new community
      insert_query = """
          INSERT INTO Community(gameID, communityID, dashboardID))
          VALUES (?, ?, ?)
          """
      cur.execute(insert_query, (gameID, communityID, dashboardID))
      conn.commit()
      print("Your new community has been added.")


  except sqlite3.Error as e:
      print(f"An error occurred: {e}")
      conn.rollback()