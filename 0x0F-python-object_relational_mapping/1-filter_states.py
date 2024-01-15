#!/usr/bin/python3
"""Defines a function that lists states
starting with letter N
"""
import sys
import MySQLdb


def filter_states(user, passwd, db):
    """Lists states starting with N"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=user, passwd=passwd,
                           db=db, charset='utf8')
    cur = conn.cursor()
    p = "SELECT * FROM states WHERE BINARY name REGEXP '^N';"
    cur.execute(p)
    names = cur.fetchall()
    for name in names:
        print(name)

    cur.close()
    conn.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    filter_states(username, password, db)
