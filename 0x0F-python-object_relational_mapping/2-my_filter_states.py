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
    sql = ("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
           .format(argv[4]))
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
