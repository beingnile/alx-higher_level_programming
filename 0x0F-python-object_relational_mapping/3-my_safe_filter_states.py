#!/usr/bin/python3

"""
The script prints states where the name matches the
fourth argument from the database hbtn_0e_0_usa
The username. password and database are passed as arguments
"""

import MySQLdb
from sys import argv


def main():
    """Run script if name == main"""
    mydb = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = mydb.cursor()
    sql = ("SELECT * FROM states")
    cursor.execute(sql)
    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)


if __name__ == '__main__':
    main()
