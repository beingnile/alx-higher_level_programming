#!/usr/bin/python3
"""Lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'

    conn = MySQLdb.connect(user=user, host=host, port=3306, passwd=pwd, db=db)
    cur = conn.cursor()

    cur.execute('SELECT id, name \
                FROM states \
                WHERE name LIKE \'N%\' \
                ORDER BY id ASC')
    names = cur.fetchall()
    for name in names:
        print(name)

    cur.close()
    conn.close()
