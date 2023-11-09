import sqlite3
import mysql.connector

# Connect to the SQLite database
sqlite_conn = sqlite3.connect('sqlite_db.db')

# Fetch data from SQLite table
cursor = sqlite_conn.execute('SELECT * FROM your_table')
data_to_migrate = cursor.fetchall()

# Connect to the MySQL database
mysql_conn = mysql.connector.connect(
    host='your_host',
    user='your_user',
    passwd='your_password',
    database='your_database'
)
mysql_cursor = mysql_conn.cursor()

# Create a MySQL table
mysql_cursor.execute('CREATE TABLE IF NOT EXISTS your_table (column1 INT, column2 VARCHAR(255))')

# Insert data into the MySQL table
mysql_cursor.executemany('INSERT INTO your_table (column1, column2) VALUES (%s, %s)', data_to_migrate)

# Commit changes and close connections
mysql_conn.commit()
mysql_cursor.close()
mysql_conn.close()
sqlite_conn.close()