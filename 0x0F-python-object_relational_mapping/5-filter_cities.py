#!/usr/bin/python3
"""Takes in the name of a state as an argument
and lists all cities of that state"""
import sys
import MySQLdb


def cities_by_state(user, passwd, db, name):
    """Prints cities matching name"""
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=user, passwd=passwd,
                           db=db, charset='utf8')
    cur = conn.cursor()
    p = """SELECT cities.name
    FROM states JOIN cities ON
    states.id = cities.state_id
    WHERE BINARY states.name = %s
    ORDER BY cities.id ASC;"""
    cur.execute(p, (name,))
    rows = cur.fetchall()
    my_list = []
    for row in rows:
        my_list.append(row[0])

    print(', '.join(my_list))

    cur.close()
    conn.close()


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    cities_by_state(user, passwd, db, name)
