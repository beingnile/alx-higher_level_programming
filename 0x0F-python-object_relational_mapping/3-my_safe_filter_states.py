#!/usr/bin/python3
"""Takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches
the argument"""
import sys
import MySQLdb


def my_filter_states(user, passwd, db, name):
    """Displays all values where name === name"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=user, passwd=passwd,
                           db=db, charset='utf8')
    cur = conn.cursor()
    p = """SELECT * FROM states
    WHERE BINARY name = %s
    ORDER BY id ASC"""
    cur.execute(p, (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    my_filter_states(user, passwd, db, name)
