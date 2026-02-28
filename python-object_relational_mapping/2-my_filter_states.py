#!/usr/bin/python3
"""List states matching a user-provided name (unsafe version)."""

import sys

import MySQLdb


if __name__ == "__main__":
    # Connect to MySQL with command-line credentials.
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = connection.cursor()

    # Required by task: build query using format with user input.
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    ).format(sys.argv[4])
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()
