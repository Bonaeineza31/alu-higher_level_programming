#!/usr/bin/python3
"""
3-my_safe_filter_states.py
Displays all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument provided
by the user, safely from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Use parameterized query to safely get the states
    query = (
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    )
    cur.execute(query, (state_name,))

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
