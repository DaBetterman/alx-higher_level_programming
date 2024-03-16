#!/usr/bin/python3
"""

"""

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', port=3306, password=sys.argv[1], user=sys.argv[2], database=sys.argv[3])
cursor = db.cursor()
query = 'SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC'
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
	print(row)
cursor.close()
db.close()
