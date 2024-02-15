#!/usr/bin/python3
"""
Get all states from database hbtn_0e_0_usa
usage 0-select_states.py\
    <database user name>\
    <database password>\
    <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    connection = MySQLdb.connect(
        user=args[1],
        password=args[2],
        database=args[3]
        )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states`")
    for state in cursor.fetchall():
        print(state)
