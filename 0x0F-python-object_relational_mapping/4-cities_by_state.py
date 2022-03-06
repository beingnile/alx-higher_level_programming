#!/usr/bin/python3

"""
The script prints all cities from the database hbtn_0e_4_usa
The username. password and database are passed as arguments
"""

import MySQLdb
from sys import argv


def main():
    """Run script if name == main"""
    mydb = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = mydb.cursor()
    sql = ("SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
