#!/usr/bin/python3
"""
lists all cities in database hbtn_0e_4_usa
usage : ./file name\
        <mysql user name>\
        <mysql password>\
        <database name>\
        <state name>
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
    cursor.execute("SELECT *\
                   FROM `cities`\
                   INNER JOIN `states`\
                   ON `cities`.`state_id` = `states`.`id`\
                   ORDER BY `cities`.`id`")
    print(", ".join(
        [city[2] for city in cursor.fetchall() if city[4] == sys.argv[4]]))
