#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
 Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])

cursor = db.cursor()
cursor.execute("SELECT * FROM states")

rows = cursor.fetchall()

for row in rows:
	print(row)

cursor.close()
db.close()


"""
MySQLdb
to connect: (host, port, user, password, database) into a database variable (db)
db.cursor
rows = cursor.fetchall()
"""
