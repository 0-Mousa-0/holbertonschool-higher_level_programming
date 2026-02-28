#!/usr/bin/python3
"""List all states from a MySQL database."""

import sys

import MySQLdb


if __name__ == "__main__":
    # Connect to the local MySQL server using provided credentials.
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = connection.cursor()

    # Fetch all states sorted by primary key.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()
