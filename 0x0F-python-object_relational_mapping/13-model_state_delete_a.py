#!/usr/bin/python3

"""
doc
"""

from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(sys.argv[1],
                           sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if 'a' in state.name:
            session.delete(state)
    session.commit()
