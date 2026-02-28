#!/usr/bin/python3
"""List states matching a user-provided name safely."""

import sys

import MySQLdb


if __name__ == "__main__":
    # Connect to the MySQL server on localhost:3306.
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = connection.cursor()

    # Use parameter binding to prevent SQL injection.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()
