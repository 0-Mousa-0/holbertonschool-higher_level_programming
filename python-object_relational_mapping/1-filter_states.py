#!/usr/bin/python3
"""List states with names starting with upper-case N."""

import sys

import MySQLdb


if __name__ == "__main__":
    # Open database connection with command-line credentials.
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = connection.cursor()

    # BINARY keeps the prefix match case-sensitive.
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()
