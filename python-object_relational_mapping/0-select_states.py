#!/usr/bin/python3
"""new project python
connect with sql server
mysql commands"""
import MySQLdb

if "__main__" == __name__:

    db = MySQLdb.connect(host='localhost', port=3306, database='hbtn_0e_0_usa', user='alejandro', password='')

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    states = cur.fetchall()
    for i in states:
        print (i)
    cur.close()
    db.close()
    