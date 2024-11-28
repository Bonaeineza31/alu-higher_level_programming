#!/usr/bin/python3
"""
2-my_filter_states.py
Displays all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument provided by the user.
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

    # Create and execute the SQL query using format() for user input
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)
    cur.execute(query)

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
