#!/usr/bin/python3
"""Start link class to table in database
"""

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2],
                            argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    statecity = City(name="San Francisco")
    state.cities = [statecity]
    session.add(state)
    session.commit()
    session.close()
