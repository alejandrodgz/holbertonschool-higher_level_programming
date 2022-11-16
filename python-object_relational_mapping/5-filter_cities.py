#!/usr/bin/python3
'''sql statements in python using
MySQLdb module'''

import MySQLdb
import sys

if "__main__" == __name__:
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[2],
        database=sys.argv[3],
        password="")

    cur = db.cursor()
    mysql_statement = "SELECT cities.name \
        FROM cities LEFT JOIN states\
        ON cities.state_id = states.id WHERE states.name = %s"
    parameters = (sys.argv[4],)
    cur.execute(mysql_statement, parameters)
    cities = cur.fetchall()
    sep = ""
    for i in cities:
        print(sep, i[0], end="")
        sep = ","
    print("")
    cur.close()
    db.close()
