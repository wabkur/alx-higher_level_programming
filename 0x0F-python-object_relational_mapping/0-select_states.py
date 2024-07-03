#!/usr/bin/python3
"""
This is a script that lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db_connect = MySQLdb.connect(
        host="localhost", user=sys[1], port=3306, passwd=sys[2], db=sys[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
