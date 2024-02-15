#!/usr/bin/python3
"""
Get all states (start with upper N) from database hbtn_0e_0_usa

usage 0-select_states.py\
    <database user name>\
    <database password>\
    <database name>\
    <state name search>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states` WHERE BINARY name = '{}'".format(
        sys.argv[4]))
    for state in cursor.fetchall():
        print(state)
