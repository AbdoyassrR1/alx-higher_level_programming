#!/usr/bin/python3
# delete all State objects with a name containing letter a

if __name__ == "__main__":
    from sqlalchemy.engine import create_engine
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import Session
    from model_state import Base, State
    import sys

    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for query in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(query)
    session.commit()
