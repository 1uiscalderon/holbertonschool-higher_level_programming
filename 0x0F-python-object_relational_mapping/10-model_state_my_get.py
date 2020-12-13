#!/usr/bin/python3
"""Start link class to table in database
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2],
                            argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        first_state = session.query(State).order_by(State.id).\
            filter(State.name == argv[4]).first()
        print(first_state.id)
    except Exception:
        print("Not found")
    session.close()
