import mysql.connector
import csv
import os

def import_csv_to_mysql(db_config, folder_path):
    # Connect to the database
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    cursor = conn.cursor()

    try:
        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

        # Iterate over all CSV files in the given folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                table_name = file_name[:-4]  # Remove '.csv' from the file name to get the table name
                csv_file_path = os.path.join(folder_path, file_name)

                # Print the current table being imported
                print(f"Importing data into {table_name} from {csv_file_path}")

                # Open the CSV file
                with open(csv_file_path, 'r') as file:
                    csv_data = csv.reader(file)

                    # Skip the header row
                    next(csv_data)

                    # Insert CSV data into the database
                    for row in csv_data:
                        placeholders = ', '.join(['%s'] * len(row))
                        query = f'INSERT INTO {table_name} VALUES ({placeholders})'
                        cursor.execute(query, row)

        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

        # Commit the transaction
        conn.commit()

    except mysql.connector.Error as err:
        # Rollback in case of error
        print("Error occurred:", err)
        conn.rollback()

    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '291878113',
    'database': 'Game_Lib'
}

# Folder path containing CSV files
# Replace this with the path to the folder containing your CSV files
folder_path = '.'

import_csv_to_mysql(db_config, folder_path)

print("Data import process completed.")
