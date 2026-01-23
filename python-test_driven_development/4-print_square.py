#!/usr/bin/python3
"""
this module is to print squares
"""


def print_square(size):
    """
    :param size: size of the square rows & columns
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        pass
    if size > 0:
        for i in range(size):
            print("#" * size)
