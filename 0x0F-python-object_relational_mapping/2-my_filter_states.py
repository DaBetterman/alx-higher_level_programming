#!/usr/bin/python3
"""
takes in an argument
 and displays all values
 in the states table of
 hbtn_0e_0_usa where name matches the argument
 Usage: ./2-my_filter_states.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name searched>
"""

import MySQLdb
import sys

if __name__ == "__main__":
	db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
	cursor = db.cursor()
	query = 'SELECT * FROM states WHERE name = "{}" ORDER BY id ASC'.format(sys.argv[4])
	cursor.execute(query)
	rows = cursor.fetchall()
	for row in rows:
		print(row)
	cursor.close()
	db.close()
