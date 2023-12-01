import mysql.connector

def view_menu(conn, user_id):
  while True:
    print("\n----------- View Menu -----------")
    print("1. View game")
    print("2. View publisher")
    print("3. View Achievement")
    print("4. View category")
    print("5. View community")
    print("6. View Dashboard")
    print("7. View all game related information(1-5 included)")
    print("8. Return")
    print("----------- View Menu ------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_game(conn,user_id)
    elif choice == "2":
        view_publisher(conn,user_id)
    elif choice == "3":
        view_achievemnt(conn,user_id)
    elif choice == "4":
        view_category(conn,user_id)
    elif choice == "5":
        view_community(conn,user_id)
    elif choice == "6":
        view_dashboard(conn,user_id)
    elif choice == "7":
        view_game_all(conn,user_id)
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")


def view_game(conn, user_id):
  """
  View game information.
  """
  while True:
      print("\n----------- View Game Menu -----------")
      print("1. View all games")
      print("2. View game by category")
      print("3. View sorted game")
      print("4. Return")
      print("----------- View Game Menu ------------")
      choice = input("Enter your choice: ")
      if choice == "1":
        gamelist = view_gamelist(conn)
        if gamelist:
            for row in gamelist:
              print(row)
        else:
            print("No game found.")
      elif choice == "2":
          gamelist_category = view_gameCate(conn)
          if gamelist_category:
            for row in gamelist_category:
              print(row)
          else:
            print("No game found.")
      elif choice == "3":
          gamelist_sorted = view_sortedGame(conn, user_id)
          if gamelist_sorted:
            for row in gamelist_sorted:
              print(row)
          else:
            print("No game found.")
      elif choice == "4":
          break
      else:
          print("Invalid choice. Please try again.")

def view_gamelist(conn):
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Game")
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()  

def view_gameCate(conn):
  try:
    cur = conn.cursor()
    category = input("Enter a category: ")
    cur.execute("SELECT * FROM Game WHERE mainCate = %s",(category,))
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_sortedGame(conn,user_id):
  while True:
    print("\n----------- Sort Menu -----------")
    print("1. sort by price")
    print("2. sort by year")
    print("3. sort by name")
    print("4. sort by category")
    print("5. Return")
    print("----------- View_Game Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Game ORDER BY price")
        rows = cur.fetchall()
        return rows
      except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    elif choice == "2":
      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Game ORDER BY `release`")
        rows = cur.fetchall()
        return rows
      except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    elif choice == "3":
      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Game ORDER BY title")
        rows = cur.fetchall()
        return rows
      except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    elif choice == "4":
      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Game ORDER BY mainCate")
        rows = cur.fetchall()
        return rows
      except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

def view_publisher(conn,user_id):
    while True:
      print("\n----------- View Publisher Menu -----------")
      print("1. View all publishers")
      print("2. View sorted publisher")
      print("3. Return")
      print("----------- View Publisher Menu ------------")
      choice = input("Enter your choice: ")
      if choice == "1":
        publisherlist = view_publisherlist(conn)
        if publisherlist:
            for row in publisherlist:
              print(row)
        else:
            print("No publisher found.")
      elif choice == "2":
          publisher_sorted = view_sortedP(conn, user_id)
          if publisher_sorted:
            for row in publisher_sorted:
              print(row)
          else:
            print("No publisher found.")
      elif choice == "3":
          break
      else:
          print("Invalid choice. Please try again.")

def view_publisherlist(conn):
    try:
      cur = conn.cursor()
      cur.execute("SELECT * FROM Publisher")
      rows = cur.fetchall()
      return rows
    except mysql.connector.Error as e:
      print(f"An error occurred: {e}")
      conn.rollback()  

def view_sortedP(conn, user_id):
  while True:
    print("\n----------- Sort Menu -----------")
    print("1. sort by name")
    print("2. sort by year")
    print("3. Return")
    print("----------- View_Publisher Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Publisher ORDER BY name")
        rows = cur.fetchall()
        return rows
      except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    elif choice == "2":
      try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Publisher ORDER BY year")
        rows = cur.fetchall()
        return rows
      except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

def view_achievemnt(conn,user_id):
  while True:
    print("\n----------- View Achievement Menu -----------")
    print("1. View all Achievement")
    print("2. View specific game achievements")
    print("3. View sorted achievements by gameID")
    print("4. Return")
    print("----------- View Achievement Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      achievement = view_alist(conn)
      if achievement:
          for row in achievement:
            print(row)
      else:
          print("No Achievement found.")
    elif choice == "2":
        specificA = view_specificA(conn)
        if specificA:
          for row in specificA:
            print(row)
        else:
          print("No Achievement found.")
    elif choice == "3":
      sortedA = view_sortedA(conn)
      if sortedA:
        for row in sortedA:
          print(row)
      else:
        print("No Achievement found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

def view_alist(conn):
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Achievement")
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()  

def view_specificA(conn):
  try:
    cur = conn.cursor()
    gameID = input("Enter a gameID: ")
    cur.execute("SELECT * FROM Achievement WHERE gameID = %s",(gameID,))
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_sortedA(conn):
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Achievement ORDER BY gameID")
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_category(conn,user_id):
  while True:
    print("\n----------- View Category Menu -----------")
    print("1. View all subcategory")
    print("2. View specific mainCate's subCategory")
    print("3. Return")
    print("----------- View Categeory Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      cate = view_allcate(conn)
      if cate:
          print("subcate, maincate")
          for row in cate:
            print(row)
      else:
          print("No subcategory found.")
    elif choice == "2":
        specificCate = view_specificCate(conn)
        if specificCate:
          for row in specificCate:
            print(row)
        else:
          print("No subcategory found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

def view_allcate(conn):
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Category")
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_specificCate(conn):
  try:
    cur = conn.cursor()
    cate = input("Enter a main category:")
    cur.execute("SELECT subCate FROM Category WHERE mainCate = %s",(cate,))
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_community(conn,user_id):
  while True:
    print("\n----------- View Communnity Menu -----------")
    print("1. View all Community")
    print("2. View specific comummnity by gameID")
    print("3. Return")
    print("----------- View Community Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      community = view_allcommun(conn)
      if community:
          for row in community:
            print(row)
      else:
          print("No community found.")
    elif choice == "2":
        specificCommun = view_specificCommun(conn)
        if specificCommun:
          for row in specificCommun:
            print(row)
        else:
          print("No community found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

def view_allcommun(conn):
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Community")
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_specificCommun(conn):
  try:
    cur = conn.cursor()
    gameID = input("Enter a gameID:")
    cur.execute("SELECT * FROM Community WHERE gameID = %s",(gameID,))
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_dashboard(conn,user_id):
  while True:
    print("\n----------- View Dashboard Menu -----------")
    print("1. View all dashboard")
    print("2. View specific Dashboard by communityID")
    print("3. Return")
    print("----------- View Dashboard Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      dashboard = view_alldash(conn)
      if dashboard:
          for row in dashboard:
            print(row)
      else:
          print("No dashboard found.")
    elif choice == "2":
        specificDash = view_specificDash(conn)
        if specificDash:
          for row in specificDash:
            print(row)
        else:
          print("No dashboard found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

def view_alldash(conn):
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Dashboard")
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_specificDash(conn):
  try:
    cur = conn.cursor()
    communityID = input("Enter a communityID:")
    cur.execute("SELECT * FROM Community c, Dashboard d WHERE c.communityID = %s AND c.dashboardID = d.dashboardID",(communityID,))
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

def view_game_all(conn,user_id):
  while True:
    print("\n----------- View All Game related all info Menu -----------")
    print("1. View all that include game, publisher, achievement, category, commnity")
    print("2. View specific a specific game's info of game, publisher, achievement, category, commnity")
    print("3. Return")
    print("----------- View All Game related all info Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      info = view_allinfo(conn)
      if info:
          print("Game Title, Publisher Name, Game achievementID, subCate, communityID, userID_likes_the_game")
          for row in info:
            print(row)
      else:
          print("No game info found.")
    elif choice == "2":
        specificinfo = view_specificinfo(conn)
        if specificinfo:
          print("Game Title, Publisher Name, Game achievementID, subCate, communityID, userID_likes_the_game")
          for row in specificinfo:
            print(row)
        else:
          print("No game info found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

def view_allinfo(conn):
  try:
    cur = conn.cursor()
    query = "SELECT g.Title, p.name, a.achievementID, cate.subCate, c.communityID, wu.userID FROM Game g, Publisher p, Achievement a, Category cate, Community c, WishlistUser wu, WishlistGame wg WHERE g.publisherID = p.publisherID AND a.gameID = g.gameID AND g.mainCate = cate.mainCate AND g.gameID = c.gameID AND g.gameID = wg.gameID AND wg.wishlistID = wu.wishlistID"
    cur.execute(query)
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def view_specificinfo(conn):
  try:
    cur = conn.cursor()
    gameTitle = input("Enter a game name:")
    query = "SELECT g.Title, p.name, a.achievementID, cate.subCate, c.communityID, wu.userID FROM Game g, Publisher p, Achievement a, Category cate, Community c, WishlistUser wu, WishlistGame wg WHERE g.title = %s AND g.publisherID = p.publisherID AND a.gameID = g.gameID AND g.mainCate = cate.mainCate AND g.gameID = c.gameID AND g.gameID = wg.gameID AND wg.wishlistID = wu.wishlistID"
    cur.execute(query,(gameTitle,))
    rows = cur.fetchall()
    return rows
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()
