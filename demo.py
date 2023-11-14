import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def list_customers(conn):
    """Query all rows in the Customer table."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM Customer")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def add_customer(conn, customer):
    """Add a new customer to the Customer table."""
    sql = '''INSERT INTO Customer(customerID, fname, lname, income, birthday)
             VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()
    return cur.lastrowid

def list_transactions_for_customer(conn, customer_id):
    """List transactions for a specific customer."""
    sql = '''
    SELECT Transactions.txnno, Transactions.amount
    FROM Transactions
    INNER JOIN Account ON Transactions.accno = Account.accno
    INNER JOIN Owns ON Account.accno = Owns.accno
    WHERE Owns.customerID = ?
    '''
    cur = conn.cursor()
    cur.execute(sql, (customer_id,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

# Example usage
conn = create_connection("demo_data.db")

# List all customers
print("Listing all customers:")
list_customers(conn)

# List transactions for a specific customer
print("Transactions for customer with ID 101:")
list_transactions_for_customer(conn, 20)

# Close the connection
conn.close()
