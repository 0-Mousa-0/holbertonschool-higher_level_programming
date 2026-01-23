#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats
    Returns an integer
    """
    if not isinstance(a, (int, float)) or a == float('inf' or '-inf') or a != a:
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)) or b == float('inf' or '-inf') or b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
