#!/usr/bin/python3
"""
This script connects to a MySQL database and
 retrieves all rows from the 'states' table where
 the state name matches the provided argument,
 using parameterized queries to prevent SQL
 injection vulnerabilities.
 Usage: ./3-my_safe_filter_states.py <mysql username>
 									 <mysql password>
									 <database name>
									 <state name searched>
"""

import MySQLdb
import sys

if __name__ == "__main__":
	db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
	cursor = db.cursor()
	query = 'SELECT * FROM states WHERE name = %s ORDER BY id ASC'
	cursor.execute(query, (sys.argv[4],))
	rows = cursor.fetchall()
	for row in rows:
		print(row)
	cursor.close()
	db.close()
