#!/usr/bin/python3
"""Delete all State rows whose name contains letter 'a'."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    # Connect to MySQL on localhost via SQLAlchemy.
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = (
        session.query(State).
        filter(State.name.like("%a%")).
        all()
    )
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
