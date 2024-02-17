#!/usr/bin/python3
"""
write a script safe form SQL injection
usage file name\
    <database user name>\
    <database password>\
    <database name>\
    <name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states`")
    for state in cursor.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
