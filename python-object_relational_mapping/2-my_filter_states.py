#!/usr/bin/python3
"""new project python
connect with sql server
mysql commands"""
import MySQLdb
import sys

if "__main__" == __name__:

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        database=sys.argv[3],
        user=sys.argv[2],
        password="")

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name ='{}' ORDER BY states.id ASC;".format(sys.argv[4]))
    states = cur.fetchall()
    for i in states:
            print(i)
    cur.close()
    db.close()
