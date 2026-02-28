#!/usr/bin/python3
"""List all cities of a given state (injection-safe)."""

import sys

import MySQLdb


if __name__ == "__main__":
    # Connect to MySQL server on localhost using provided arguments.
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = connection.cursor()

    # One parameterized query for safe state filtering.
    cursor.execute(
        "SELECT cities.name "
        "FROM cities INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],),
    )
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    connection.close()
