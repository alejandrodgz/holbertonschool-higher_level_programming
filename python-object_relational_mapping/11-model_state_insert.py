@@ -0,0 +1,23 @@
#!/usr/bin/python3
"""retrieving info from sqalchemy
no idea how"""


from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session = Session()
    new1 = State(name="Louisiana")
    Session.add(new1)
    Session.commit()
    print(new1.id)
    Session.close()