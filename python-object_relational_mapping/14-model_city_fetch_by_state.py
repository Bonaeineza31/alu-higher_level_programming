#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Displays results as <state name>: (<city id>) <city name>.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind to database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and states, sort by cities.id
    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Display results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
