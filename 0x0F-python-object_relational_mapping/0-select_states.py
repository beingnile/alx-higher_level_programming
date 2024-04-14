#!/usr/bin/python3
"""Prints all states in the hbtn_0e_0_usa database"""
from sys import argv
import MySQLdb


def select_states(user, passwd, db):
    """Connects to MySQL and executes script"""
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    select_states(user, passwd, db)
