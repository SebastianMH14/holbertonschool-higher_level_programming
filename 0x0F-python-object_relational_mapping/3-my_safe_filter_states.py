#!/usr/bin/python3
"""script that lists all
states from the database
hbtn_0e_0_usa"""

if __name__ == '__main__':

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
    cur.execute("SELECT * FROM states \
        WHERE name = (\'%s\') ORDER BY id ASC" % (namesh))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
