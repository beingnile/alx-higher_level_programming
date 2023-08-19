#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'

    conn = MySQLdb.connect(host=host, port=3306, user=user, passwd=passwd, db=db)
    cur = conn.cursor()

    cur.execute('SELECT id, name FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    conn.close()
