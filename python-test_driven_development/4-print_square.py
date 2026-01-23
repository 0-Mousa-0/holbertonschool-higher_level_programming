#!/usr/bin/python3
"""
this module is to print squares
"""


def print_square(size):
    """
    :param size: size of the square rows & columns
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
