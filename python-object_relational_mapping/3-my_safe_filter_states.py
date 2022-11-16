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
    sql_statement = "SELECT * FROM states WHERE name =%s\
    ORDER BY states.id ASC;"
    parameters = (sys.argv[4],)
    cur.execute(sql_statement, parameters)
    states = cur.fetchall()
    for i in states:
        if i[1] == sys.argv[4]:
            print(i)
    cur.close()
    db.close()
