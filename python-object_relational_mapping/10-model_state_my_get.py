#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    # Create an engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create a session maker and initialize a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object that matches the state_name_to_search
    state = session.query(State).filter(
        State.name == state_name_to_search
    ).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
