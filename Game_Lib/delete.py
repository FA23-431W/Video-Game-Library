import mysql.connector

def delete_menu(conn, user_id):
  while True:
    print("\n----------- Delete Menu -----------")
    print("1. Delete specific element")
    print("2. Delete table")
    print("3. Return")
    print("----------- Delete Menu ------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        delete_specfic(conn,user_id)
    elif choice == "2":
        delete_table(conn,user_id)
    elif choice == "3":
        # admin_menu(conn, user_id)
        break
    else:
        print("Invalid choice. Please try again.")

def delete_specfic(conn,user_id):
  while True:
      print("\n----------- Delete Record Menu -----------")
      print("1. Delete game")
      print("2. Delete publisher")
      print("3. Delete Achievement")
      print("4. Delete category")
      print("5. Delete community")
      print("6. Delete Dashboard")
      print("7. Delete user")
      print("8. Return")
      print("----------- Delete Record Menu ------------")
      choice = input("Enter your choice: ")
      if choice == "1":
          delete_game(conn)
      elif choice == "2":
          delete_publisher(conn)
      elif choice == "3":
          delete_achievemnt(conn)
      elif choice == "4":
          delete_category(conn)
      elif choice == "5":
          delete_community(conn)
      elif choice == "6":
          delete_dashboard(conn)
      elif choice == "7":
          delete_user(conn)
      elif choice == "8":
          # admin_menu(conn, user_id)
          break
      else:
        print("Invalid choice. Please try again.")
        
def delete_game(conn):
  try:
    cur = conn.cursor()
    gameID = input("Enter a gameID that want to delete:")
    cur.execute("DELETE FROM Game WHERE gameID = %s",(gameID))
    cur.execute("DELETE FROM Achievement WHERE gameID = %s", (gameID))
    cur.execute("DELETE FROM Community WHERE gameID = %s",(gameID))
    cur.execute("DELETE FROM WishlistGame WHERE gameID = %s",(gameID))
    conn.commit()
    print("Your game has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()  
    
def delete_achievemnt(conn):
  try:
    cur = conn.cursor()
    achievementID = input("Enter a achievementID that want to delete:")
    cur.execute("DELETE FROM Achievement WHERE achievementID = %s",(achievementID))
    conn.commit()
    print("Your achievement has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()  

def delete_dashboard(conn):
  try:
    cur = conn.cursor()
    dashboardID = input("Enter a dashboardID that want to delete:")
    cur.execute("DELETE FROM Dashboard WHERE dashboardID = %s",(dashboardID))
    cur.execute("UPDATE Community SET dashboardID = NULL WHERE dashboardID = %s",(dashboardID))
    conn.commit()
    print("Your dashboard has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 
  
def delete_publisher(conn):
  try:
    cur = conn.cursor()
    publisherID = input("Enter a publisherID that want to delete:")
    cur.execute("DELETE FROM Publisher WHERE publisherID = %s",(publisherID))
    cur.execute("DELETE FROM Game WHERE publisherID = %s", (publisherID))
    conn.commit()
    print("Your publisher has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_category(conn):
  try:
    cur = conn.cursor()
    cate = input("Enter a sub category that want to delete:")
    cur.execute("DELETE FROM Category WHERE subCate = %s",(cate))
    conn.commit()
    print("Your sub category has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_community(conn):
  try:
    cur = conn.cursor()
    communityID = input("Enter a communityID that want to delete:")
    cur.execute("DELETE FROM Dashboard d INNER JOIN Community c WHERE c.communityID = %s AND c.dashboardID = d.dashboardID",(communityID))
    conn.commit()
    print("Your community has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_user(conn):
  try:
    cur = conn.cursor()
    userID = input("Enter a userID that want to delete:")
    cur.execute("DELETE FROM User WHERE userID = %s",(userID))
    cur.execute("DELETE FROM WishlistUser wu INNER JOIN WishlistGame wg WHERE userID = %s AND wu.wishlistID = wg.wishlistID",(userID))
    conn.commit()
    print("Your user has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_table(conn,user_id):
  while True:
      print("\n----------- Delete Table Menu -----------")
      print("1. Delete game")
      print("2. Delete publisher")
      print("3. Delete Achievement")
      print("4. Delete category")
      print("5. Delete community")
      print("6. Delete Dashboard")
      print("7. Delete user")
      print("8. Delete wishlist")
      print("9. Return")
      print("----------- Delete Table Menu ------------")
      choice = input("Enter your choice: ")
      if choice == "1":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE game")
          cur.execute("ALTER TABLE Achievement DROP COLUMN gameID")
          cur.execute("ALTER TABLE WishlistGame DROP COLUMN gameID")
          cur.execute("ALTER TABLE Community DROP COLUMN gameID")
          conn.commit()
          print("Your game table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "2":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE Publisher")
          cur.execute("ALTER TABLE Game DROP COLUMN publisherID")
          conn.commit()
          print("Your publisher table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "3":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE Achievement")
          conn.commit()
          print("Your Achievement table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "4":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE Category")
          conn.commit()
          print("Your category table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "5":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE Community")
          conn.commit()
          print("Your community table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "6":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE Dashboard")
          cur.execute("ALTER TABLE Community DROP COLUMN dashboardID")
          conn.commit()
          print("Your dahsboard table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "7":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE User")
          cur.execute("ALTER TABLE WishlistUser DROP COLUMN userID")
          conn.commit()
          print("Your User table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "8":
        try:
          cur = conn.cursor()
          cur.execute("DROP TABLE WishlistUser")
          cur.execute("DROP TABLE WishlistGame")
          cur.execute("ALTER TABLE User DROP COLUMN wishlistID")
          conn.commit()
          print("Your Wishlist table has been deleted.")
        except mysql.connector.Error as e:
          print(f"An error occurred: {e}")
          conn.rollback() 
      elif choice == "9":
        # admin_menu(conn, user_id)
        break
      else:
        print("Invalid choice. Please try again.")
