#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the
database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create database connection
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete states with 'a' in their name
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()  # Commit changes to the database
    session.close()  # Close the session
