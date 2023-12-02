import mysql.connector

def delete_menu(conn,user_id):
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
          break
      else:
        print("Invalid choice. Please try again.")
        
def delete_game(conn):
  try:
    cur = conn.cursor()
    gameID = input("Enter a gameID that want to delete:")
    cur.execute("DELETE FROM Achievement WHERE gameID = %s", (gameID,))
    cur.execute("DELETE FROM Community WHERE gameID = %s",(gameID,))
    cur.execute("DELETE FROM WishlistGame WHERE gameID = %s",(gameID,))
    cur.execute("DELETE FROM Game WHERE gameID = %s",(gameID,))
    conn.commit()
    print("Your game has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()  
    
def delete_achievemnt(conn):
  try:
    cur = conn.cursor()
    achievementID = input("Enter a achievementID that want to delete:")
    cur.execute("DELETE FROM Achievement WHERE achievementID = %s",(achievementID,))
    conn.commit()
    print("Your achievement has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()  

def delete_dashboard(conn):
  try:
    cur = conn.cursor()
    dashboardID = input("Enter a dashboardID that want to delete:")
    cur.execute("UPDATE Community SET dashboardID = NULL WHERE dashboardID = %s",(dashboardID,))
    cur.execute("DELETE FROM Dashboard WHERE dashboardID = %s",(dashboardID,))
    conn.commit()
    print("Your dashboard has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 
  
def delete_publisher(conn):
  try:
    cur = conn.cursor()
    publisherID = input("Enter a publisherID that want to delete:")
    cur.execute("UPDATE Game SET publisherID = NULL WHERE publisherID = %s", (publisherID,))
    cur.execute("DELETE FROM Publisher WHERE publisherID = %s",(publisherID,))
    conn.commit()
    print("Your publisher has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_category(conn):
  try:
    cur = conn.cursor()
    cate = input("Enter a sub category that want to delete:")
    cur.execute("DELETE FROM Category WHERE subCate = %s",(cate,))
    conn.commit()
    print("Your sub category has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_community(conn):
  try:
    cur = conn.cursor()
    communityID = input("Enter a communityID that want to delete:")
    cur.execute("DELETE FROM Community c WHERE c.communityID = %s",(communityID,))
    conn.commit()
    print("Your community has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

def delete_user(conn):
  try:
    cur = conn.cursor()
    userID = input("Enter a userID that want to delete:")
    cur.execute("DELETE FROM WishlistUser WHERE userID = %s",(userID,))
    cur.execute("DELETE FROM User WHERE userID = %s",(userID,))
    conn.commit()
    print("Your user has been deleted.")
  except mysql.connector.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() 

