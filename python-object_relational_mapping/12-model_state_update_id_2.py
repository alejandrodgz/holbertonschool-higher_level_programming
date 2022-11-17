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
    usr_update = Session.query(State).filter(State.id == 2).first()
    usr_update.name = "New Mexico"
    Session.commit()
    Session.close()
