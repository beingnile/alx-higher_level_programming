#!/usr/bin/python3
"""Prints all states that start with N"""
from sys import argv
import MySQLdb


def filter_states(user, passwd, db):
    """Conects to MySQL and executes script

    Arguments:
    user (str): The username for the MySQL server to connect to
    passwd (str): @user's password
    db (str): The name of the database to connect to
    """
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db)
    cur = conn.cursor()
    # SQL prompt
    p = "SELECT * FROM states WHERE BINARY NAME LIKE 'N%' ORDER BY id ASC;"
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

    filter_states(user, passwd, db)
