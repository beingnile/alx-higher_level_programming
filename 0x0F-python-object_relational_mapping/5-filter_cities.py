#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb


def filter_cities(user, passwd, db, arg):
    """
    Connects to a MySQL server to get cities list

    Arguments:
    user (str): MySQL user to connect with
    passwd (str): @user's password
    db (str): The database name
    arg (str): State name to list cities of
    """
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=user,
                           passwd=passwd,
                           db=db)
    cur = conn.cursor()
    p = """
    SELECT cities.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE BINARY states.name LIKE %s;
    """
    cur.execute(p, (arg,))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])

    print(', '.join(cities))

    cur.close()
    conn.close()


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    arg = argv[4]

    filter_cities(user, passwd, db, arg)
