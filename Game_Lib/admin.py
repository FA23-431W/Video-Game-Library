import mysql.connector
from view import view_menu
from insert import insert_menu
from delete import delete_menu
from update import update_menu
from alter import alter_menu

def admin_menu(conn, user_id):
    while True:
        print("\n----------- Admin Menu -----------")
        print("1. View")
        print("2. Insert")
        print("3. Delete")
        print("4. Update")
        print("5. Alter Table")
        print("6. Logout")
        print("----------- Admin Menu ------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_menu(conn, user_id)
        elif choice == "2":
            insert_menu(conn, user_id)
        elif choice == "3":
            delete_menu(conn, user_id)
        elif choice == "4":
            update_menu(conn, user_id)
        elif choice == "5":
            alter_menu(conn, user_id)
        elif choice == "6":
            print("Logout")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    conn = create_connection()
    if conn:
    	main_menu(conn)
    	conn.close()
    else:
        print("Failed to establish a database connection.")
