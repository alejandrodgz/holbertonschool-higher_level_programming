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

    print(sys.argv[4])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name ='{}' ORDER BY states.id ASC;".format(sys.argv[4]))
    states = cur.fetchall()
    for i in states:
        if i[1] == sys.argv[4]:
            print(i)
    cur.close()
    db.close()
