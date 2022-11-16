#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class state from database
    table state"""
    __tablename__ = 'states'
    id = Column(
        "id",
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement="auto")
    name = Column("name", String(128), nullable=False)
