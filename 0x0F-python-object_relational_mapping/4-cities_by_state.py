#!/usr/bin/python3
"""script that lists all
states from the database
hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

user = argv[1]
passwd = argv[2]
db = argv[3]

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=user,
    passwd=passwd,
    db=db,
    charset="utf8")
cur = conn.cursor()
cur.execute("SELECT cities.id, cities.name, states.name  \
    FROM cities INNER JOIN states \
    ON states.id = cities.state_id \
    ORDER BY cities.id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
