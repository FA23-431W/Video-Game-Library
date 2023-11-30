import sqlite3
from admin import admin_menu

def alter_menu(conn,user_id):
  while True:
      print("\n----------- Alter Table Menu -----------")
      print("1. Alter Game")
      print("2. Alter Publisher")
      print("3. Alter Achievement")
      print("4. Alter Category")
      print("5. Alter Community")
      print("6. Alter Dashboard")
      print("7. Alter User")
      print("8. Alter WishlistUser")
      print("9. Alter WishlistGame")
      print("10. Return")
      print("----------- Alter table Menu ------------")
      choice = input("Enter your choice: ")
      if choice == "1":
          alter_game(conn,user_id)
      elif choice == "2":
          alter_publisher(conn,user_id)
      elif choice == "3":
          alter_achievemnt(conn,user_id)
      elif choice == "4":
          alter_category(conn,user_id)
      elif choice == "5":
          alter_community(conn,user_id)
      elif choice == "6":
          alter_dashboard(conn,user_id)
      elif choice == "7":
          alter_user(conn,user_id)
      elif choice == "8":
          alter_wishlistUser(conn,user_id)
      elif choice == "9":
          alter_wishlistGame(conn,user_id)
      elif choice == "10":
          admin_menu(conn, user_id)
          break
      else:
        print("Invalid choice. Please try again.")

def alter_game(conn,user_id):
  while True:
    print("\n----------- Alter Game Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter Game Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(gameID, publisherID, title, mainCate, price, release): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE Game RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your game column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Game ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your game column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(gameID, publisherID, title, mainCate, price, release):")
        cur.execute("ALTER TABLE Game DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your game column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(gameID, publisherID, title, mainCate, price, release):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Game ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your game column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_publisher(conn,user_id):
  while True:
    print("\n----------- Alter Publisher Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter Publisher Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(publisherID, name, year): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE Publisher RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your Publisher column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Publisher ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your Publisher column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(publisherID, name, year):")
        cur.execute("ALTER TABLE Publisher DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your Publisher column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(publisherID, name, year):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Publisher ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your Publisher column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_achievemnt(conn,user_id):
  while True:
    print("\n----------- Alter Achievement Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter Achievement Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(achievementID, description, gameID): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE Achievement RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your Achievement column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Achievement ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your Achievement column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(achievementID, description, gameID):")
        cur.execute("ALTER TABLE Achievement DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your Achievement column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(achievementID, description, gameID):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Achievement ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your Achievement column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_category(conn,user_id):
  while True:
    print("\n----------- Alter Category Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter Category Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(mainCate, subCate): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE Category RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your category column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Category ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your Category column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(mainCate, subCate):")
        cur.execute("ALTER TABLE Category DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your Category column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(mainCate, subCate):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Category ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your Category column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_community(conn,user_id):
  while True:
    print("\n----------- Alter Community Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter Community Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(gameID, communityID, dashboardID): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE Community RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your Community column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Community ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your Community column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(gameID, communityID, dashboardID):")
        cur.execute("ALTER TABLE Community DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your Community column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(gameID, communityID, dashboardID):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Community ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your Community column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_dashboard(conn,user_id):
  while True:
    print("\n----------- Alter Dashboard Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter Dashboard Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(dashboardID, post, date, author): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE Dashboard RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your Dashboard column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Dashboard ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your Dashboard column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(dashboardID, post, date, author):")
        cur.execute("ALTER TABLE Dashboard DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your Dashboard column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(dashboardID, post, date, author):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE Dashboard ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your Dashboard column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_user(conn,user_id):
  while True:
    print("\n----------- Alter User Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter User Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(userID, name, password, wishlistID): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE User RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your User column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE User ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your User column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(userID, name, password, wishlistID):")
        cur.execute("ALTER TABLE User DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your User column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(userID, name, password, wishlistID):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE User ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your User column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_wishlistUser(conn,user_id):
  while True:
    print("\n----------- Alter WishlistUser Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter WishlistUser Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(userID, wishlistID): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE WishlistUser RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your WishlistUser column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE WishlistUser ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your WishlistUser column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(userID, wishlistID):")
        cur.execute("ALTER TABLE WishlistUser DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your WishlistUser column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(userID, wishlistID):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE wishlistUser ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your WishlistUser column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")

def alter_wishlistGame(conn,user_id): 
  while True:
    print("\n----------- Alter WishlistGame Menu -----------")
    print("1. Change column name")
    print("2. Add column")
    print("3. Delete column")
    print("4. Modify datatype")
    print("5. Return")
    print("----------- Alter WishlistGame Menu ------------")
    choice = input("Enter your choice: ")
    if choice == "1":
      try:
        cur = conn.cursor()
        oldCol = input("Enter the column that you want to change(gameID, wishlistID): ")
        columnName = input("Enter a new column name:")
        cur.execute("ALTER TABLE WishlistGame RENAME COLUMN ? to ?",(oldCol,columnName))
        conn.commit()
        print("Your WishlistGame column has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "2":
      try:
        cur = conn.cursor()
        columnName = input("Enter a new column name:")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE WishlistGame ADD ? ?",(columnName,columnType))
        conn.commit()
        print("Your WishlistGame column has been added.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "3":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to delete(gameID, wishlistID):")
        cur.execute("ALTER TABLE WishlistGame DROP COLUMN ?",(columnName))
        conn.commit()
        print("Your WishlistGame column has been deleted.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "4":
      try:
        cur = conn.cursor()
        columnName = input("Enter the column name that want to change datatype(gameID, wishlistID):")
        columnType = input("Enter a datatype for the column: ")
        cur.execute("ALTER TABLE WishlistGame ALTER COLUMN ? ?",(columnName,columnType))
        conn.commit()
        print("Your WishlistGame column's datatype has been changed.")
      except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback() 
    elif choice == "5":
        alter_menu(conn, user_id)
        break
    else:
      print("Invalid choice. Please try again.")