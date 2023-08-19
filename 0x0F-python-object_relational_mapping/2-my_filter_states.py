#!/usr/bin/python3
"""Takes in an arg and displays all the values in the states
table in the hbtn_0e_0_usa database where name matches the arg.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    host = 'localhost'
    arg = sys.argv[4]

    conn = MySQLdb.connect(user=user, host=host, port=3306, passwd=pwd, db=db)
    cur = conn.cursor()

    cur.execute(f'SELECT id, name FROM states WHERE name LIKE \'{arg}\'')
    states = cur.fetchall()
    for state in states:
        print(state)
