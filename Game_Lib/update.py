import mysql.connector

def update_menu(conn,user_id):
  while True:
      print("\n----------- Update Menu -----------")
      print("1. Update game")
      print("2. Update publisher")
      print("3. Update Achievement")
      print("4. Update category")
      print("5. Update community")
      print("6. Update Dashboard")
      print("7. Update user")
      print("8. Return")
      print("----------- Update Menu ------------")
      choice = input("Enter your choice: ")
      if choice == "1":
          update_game(conn)
      elif choice == "2":
          update_publisher(conn)
      elif choice == "3":
          update_achievemnt(conn)
      elif choice == "4":
          update_category(conn)
      elif choice == "5":
          update_community(conn)
      elif choice == "6":
          update_dashboard(conn)
      elif choice == "7":
          update_user(conn)
      elif choice == "8":
          break
      else:
        print("Invalid choice. Please try again.")

def update_game(conn):
  try:
    cur = conn.cursor()
    gameID = input("Enter a gameID that want to update:")
    num = input("Enter the number of elements of the game that want to update:")
    for i in range(int(num)):
      element = input("Enter the element that want to update (publisherID, title, mainCate, price, release):")
      value = input("Enter the new value:")
      if element == "publisherID":
        update_query = """
            UPDATE Game
            SET publisherID = %s
            WHERE gameID = %s
            """
        cur.execute(update_query, (value, gameID))
        conn.commit()
      elif element == "title":
        update_query = """
            UPDATE Game
            SET title = %s
            WHERE gameID = %s
          """
        cur.execute(update_query, (value, gameID))
        conn.commit()
      elif element == "mainCate":
        update_query = """
            UPDATE Game
            SET mainCate = %s
            WHERE gameID = %s
          """
        cur.execute(update_query, (value, gameID))
        conn.commit()
      elif element == "price":
        update_query = """
            UPDATE Game
            SET price = %s
            WHERE gameID = %s
          """
        cur.execute(update_query, (value, gameID))
        conn.commit()
      elif element == "release":
        update_query = """
            UPDATE Game
            SET release = %s
            WHERE gameID = %s
          """
        cur.execute(update_query, (value, gameID))
        conn.commit()
      else:
        print("Invalid choice. Please try again.")
    print("Your game info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def update_publisher(conn):
  try:
    cur = conn.cursor()
    publisherID = input("Enter a publisherID that want to update:")
    num = input("Enter the number of elements of the publisher that want to update:")
    for i in range(int(num)):
      element = input("Enter the element that want to update (name, year):")
      value = input("Enter the new value:")
      if element == "name":
        update_query = """
            UPDATE Publisher
            SET name = %s
            WHERE publisherID = %s
            """
        cur.execute(update_query, (value, publisherID))
        conn.commit()
      elif element == "year":
        update_query = """
            UPDATE Publisher
            SET year = %s
            WHERE publisherID = %s
          """
        cur.execute(update_query, (value, publisherID))
        conn.commit()
      else:
        print("Invalid choice. Please try again.")
    print("Your publisher info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def update_achievemnt(conn):
  try:
    cur = conn.cursor()
    achievement = input("Enter a AchievementID that want to update:")
    num = input("Enter the number of elements of the achievement that want to update:")
    for i in range(int(num)):
      element = input("Enter the element that want to update (description, gameID):")
      value = input("Enter the new value:")
      if element == "description":
        update_query = """
            UPDATE Achievement
            SET description = %s
            WHERE achievementID = %s
            """
        cur.execute(update_query, (value, achievement))
        conn.commit()
      elif element == "gameID":
        update_query = """
            UPDATE Achievement
            SET gameID = %s
            WHERE achievementID = %s
          """
        cur.execute(update_query, (value, achievement))
        conn.commit()
      else:
        print("Invalid choice. Please try again.")
    print("Your achievement info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def update_category(conn):
  try:
    cur = conn.cursor()
    cate = input("Enter a sub category that want to update:")
    value = input("Enter the new main category:")
    update_query = "UPDATE Category SET mainCate = %sWHERE subCate = %s"
    cur.execute(update_query, (value, cate))
    conn.commit()
    print("Your category info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def update_community(conn):
  try:
    cur = conn.cursor()
    community = input("Enter a community that want to update:")
    num = input("Enter the number of elements of the community that want to update:")
    for i in range(int(num)):
      element = input("Enter the element that want to update (gameID, dashboardID):")
      value = input("Enter the new value:")
      if element == "gameID":
        update_query = """
            UPDATE Community
            SET gameID = %s
            WHERE communityID = %s
            """
        cur.execute(update_query, (value, community))
        conn.commit()
      elif element == "dashboardID":
        update_query = """
            UPDATE Community
            SET dashboardID = %s
            WHERE communnityID = %s
          """
        cur.execute(update_query, (value, community))
        conn.commit()
      else:
        print("Invalid choice. Please try again.")
    print("Your community info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def update_dashboard(conn):
  try:
    cur = conn.cursor()
    dashboard = input("Enter a dashboard that want to update:")
    num = input("Enter the number of elements of the dahsboard that want to update:")
    for i in range(int(num)):
      element = input("Enter the element that want to update (post, date, author):")
      value = input("Enter the new value:")
      if element == "post":
        update_query = """
            UPDATE Dashboard
            SET post = %s
            WHERE dashboardID = %s
            """
        cur.execute(update_query, (value, dashboard))
        conn.commit()
      elif element == "date":
        update_query = """
            UPDATE Dashboard
            SET date = %s
            WHERE dashbardID = %s
          """
        cur.execute(update_query, (value, dashboard))
        conn.commit()
      elif element == "author":
        update_query = """
            UPDATE Dashboard
            SET author = %s
            WHERE dashbardID = %s
          """
        cur.execute(update_query, (value, dashboard))
        conn.commit()
      else:
        print("Invalid choice. Please try again.")
    print("Your community info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def update_user(conn):
  try:
    cur = conn.cursor()
    user = input("Enter a user that want to update:")
    num = input("Enter the number of elements of the user that want to update:")
    for i in range(int(num)):
      element = input("Enter the element that want to update (name,password,wishlistID):")
      value = input("Enter the new value:")
      if element == "name":
        update_query = """
            UPDATE User
            SET name = %s
            WHERE userID = %s
            """
        cur.execute(update_query, (value, user))
        conn.commit()
      elif element == "password":
        update_query = """
            UPDATE User
            SET password = %s
            WHERE userID = %s
          """
        cur.execute(update_query, (value, user))
        conn.commit()
      elif element == "wishlistID":
        update_query = """
            UPDATE User
            SET wishlistID = %s
            WHERE userID = %s
          """
        cur.execute(update_query, (value, user))
        update_query = """
            UPDATE WishlistUser
            SET wishlistID = %s
            WHERE userID = %s
          """
        cur.execute(update_query, (value, user))
        conn.commit()
      else:
        print("Invalid choice. Please try again.")
    print("Your community info has updated.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

