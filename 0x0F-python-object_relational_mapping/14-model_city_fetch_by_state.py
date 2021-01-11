#!/usr/bin/python3
"""Start link class to table in database
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2],
                            argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).join(State).\
            order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()