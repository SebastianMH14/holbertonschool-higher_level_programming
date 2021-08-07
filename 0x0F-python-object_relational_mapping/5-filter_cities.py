#!/usr/bin/python3
"""script that lists all
states from the database
hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

user = argv[1]
passwd = argv[2]
db = argv[3]
namesh = argv[4]

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=user,
    passwd=passwd,
    db=db,
    charset="utf8")
cur = conn.cursor()
cur.execute("SELECT cities.name  \
    FROM cities INNER JOIN states \
    ON states.id = cities.state_id \
    WHERE states.name = (\'%s\') \
    ORDER BY cities.id ASC"  % (namesh))
query_rows = cur.fetchall()
for row in query_rows:
    print(row[0], end=", ")
print()
cur.close()
conn.close()
