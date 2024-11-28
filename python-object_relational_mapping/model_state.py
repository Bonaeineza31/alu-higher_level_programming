#!/usr/bin/python3
"""
Defines a State class and creates the `states` table in the database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative_base
Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database table.

    Attributes:
        id (int): The state's id, primary key, auto-generated.
        name (str): The state's na 128 characters.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(
        String(128),
        nullable=False
    )


if __name__ == "__main__":
    import sys

    # Connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Create all tables in the database
    Base.metadata.create_all(engine)
