#!/usr/bin/python3
"""List all State rows whose name contains letter 'a'."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    # Open SQLAlchemy connection to local MySQL.
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Filter state names that contain lowercase 'a'.
    states = session.query(State).filter(State.name.like("%a%")).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
