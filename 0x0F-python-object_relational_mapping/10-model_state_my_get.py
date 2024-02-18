#!/usr/bin/python3
"""
list all states using sqlalchemy
with the name passed as argument from the database hbtn_0e_6_usa
the script take 4 args
usage file name <mysql user name>\
                <mysql password>\
                <database name>\
                <name searched>
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

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")
