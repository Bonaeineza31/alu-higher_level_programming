#!/usr/bin/python3
"""
5-filter_cities.py
Lists all cities from the `cities` table of `hbtn_0e_4_usa` 
where `state name` matches the argument provided by the user.
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

    # SQL query to fetch cities where state name  user input
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    
    # Execute the query with safe parameterized input
    cur.execute(query, (state_name,))

    # Fetch and display the results
    rows = cur.fetchall()
    
    if rows:
        print(", ".join([row[0] for row in rows]))
    else:
        print("")

    # Close cursor and database connection
    cur.close()
    db.close()
