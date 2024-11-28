#!/usr/bin/python3
"""
Select all records from states table
"""

#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Display each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
