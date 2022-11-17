#!/usr/bin/python3
"""retrieving info from sqalchemy
no idea how"""


from model_state import Base, State
import sys
from sqlalchemy import (create_engine, update)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session = Session()
    new_upt = update(State).where(State.id==2).values(name='New Mexico')
    Session.add(new_upt)
    Session.commit()
    Session.close()