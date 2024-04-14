#!/usr/bin/python3
"""Prints states matching an argument passed from
the table states in the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb


def filter_states_by_arg(user, passwd, db, arg):
    """Connects to a MySQL server and executes commands"""
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db)
    cur = conn.cursor()
    p = "SELECT * FROM states WHERE BINARY name LIKE '{}';".format(arg)
    cur.execute(p)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    arg = argv[4]

    filter_states_by_arg(user, passwd, db, arg)
