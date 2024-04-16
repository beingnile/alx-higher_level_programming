#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb


def cities_by_state(user, passwd, db):
    """
    Connects to a MySQL server to get cities list

    Arguments:
    user (str): MySQL user to connect server with
    passwd (str): The user's password
    db (str) : The database name to connect to
    """
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db)
    cur = conn.cursor()
    p = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
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

    cities_by_state(user, passwd, db)
