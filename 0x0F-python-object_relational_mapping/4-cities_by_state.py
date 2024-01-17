#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


def cities_by_state(user, passwd, db):
    """Prints cities and states"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=user, passwd=passwd,
                           db=db, charset='utf8')
    cur = conn.cursor()
    p = """SELECT cities.id, cities.name, states.name
    FROM states JOIN cities ON
    states.id = cities.state_id;"""
    cur.execute(p)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    cities_by_state(user, passwd, db)
