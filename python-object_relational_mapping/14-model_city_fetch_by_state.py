#!/usr/bin/python3
"""Print all cities with their related state name using SQLAlchemy."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the target MySQL database with SQLAlchemy engine.
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Join states and cities, then print in required output format.
    rows = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    for state_name, city_id, city_name in rows:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
