#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
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

    # Create and add the new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new state
    print(new_state.id)

    # Close the session
    session.close()
