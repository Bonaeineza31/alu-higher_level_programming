#!/usr/bin/python3
"""
Lists all State objects containing the
letter 'a' from the database hbtn_0e_6_usa.
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
            mysql_username, mysql_password, database_name),
        pool_pre_ping=True,
    )

    # Create a session maker and initialize a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects that contain the letter 'a'
    states_with_a = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
