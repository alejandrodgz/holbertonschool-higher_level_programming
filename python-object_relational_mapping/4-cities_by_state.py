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
    mysql_statement = "SELECT * FROM cities ORDER BY id ASC"
    cur.execute(mysql_statement)
    cities = cur.fetchall()
    for i in cities:
        print(i)
    cur.close()
    db.close()
