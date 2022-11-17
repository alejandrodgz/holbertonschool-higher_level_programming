#!/usr/bin/python3
"""new class named city
inherits from Base as State do"""

import model_state
from sqlalchemy import Column, Integer, String, ForeignKey

class City(model_state.Base):
    __tablename__ = "cities"
    id = Column("id", Integer, nullable=False, primary_key=True,
         autoincrement = "auto", unique=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id",
              Integer, ForeignKey("states.id"), nullable=False)
