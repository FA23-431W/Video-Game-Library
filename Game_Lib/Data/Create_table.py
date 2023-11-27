import csv
import sqlite3
import os
import pandas as pd



def get_csv_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.csv')]

def create_table_name(csv_file):
    return os.path.splitext(csv_file)[0]


conn = sqlite3.connect('data.db')
cursor = conn.cursor()

csv_directory = '.'
for csv_file in get_csv_files(csv_directory):
    df = pd.read_csv(os.path.join(csv_directory, csv_file))
    table_name = create_table_name(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
