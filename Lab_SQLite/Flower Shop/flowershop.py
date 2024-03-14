import sqlite3

# Connect to the database
conn = sqlite3.connect('c:\\Users\\prajv\\Desktop\\Sourcecode\\Python II\\Lab_SQLite\\Flower Shop\\flowershop.db')

#Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute("INSERT INTO Products VALUES('Flower3', 'Lavender', 'Shelf 2', 100, 10)")

conn.commit()

conn.close()