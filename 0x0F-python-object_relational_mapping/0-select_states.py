#!/usr/bin/python3
"""Defines a function that lists all states
from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def select_states(user, passwd, db):
    """Lists all states from the database
    hbtn_0e_0_usa"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=user, passwd=passwd,
                           db=db, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    select_states(username, password, db)
