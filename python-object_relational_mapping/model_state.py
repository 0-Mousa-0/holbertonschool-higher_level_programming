#!/usr/bin/python3
"""State model definition for SQLAlchemy ORM mapping."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


# Base class for all ORM-mapped classes in this project.
Base = declarative_base()


class State(Base):
    """Represent a state row in the `states` table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
