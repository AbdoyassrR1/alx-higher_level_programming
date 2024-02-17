#!/usr/bin/python3
"""
lists all cities in database hbtn_0e_4_usa
usage : ./file name\
        <mysql user name>\
        <mysql password>\
        <database name>
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
    cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                   FROM `cities`\
                   INNER JOIN `states`\
                   ON `cities`.`state_id` = `states`.`id`\
                   ORDER BY `cities`.`id`")
    for city in cursor.fetchall():
        print(city)
