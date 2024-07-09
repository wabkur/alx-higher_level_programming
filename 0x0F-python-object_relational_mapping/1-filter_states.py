#!/usr/bin/python3
"""lists all states name with N from the database."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )

    cu = db.cursor()
    cu.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cu.fetchall()
    for r in rows:
        print(r)
    cu.close()
    db.close()