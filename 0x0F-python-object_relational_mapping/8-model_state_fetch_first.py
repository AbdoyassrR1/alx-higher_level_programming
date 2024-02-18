#!/usr/bin/python3
"""
list first states using sqlalchemy
the script take 3 args
usage file name <mysql user name>\
                <mysql password>\
                <database name>
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

    first_result = session.query(State).order_by(State.id).first()
    if first_result is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_result.id, first_result.name))
