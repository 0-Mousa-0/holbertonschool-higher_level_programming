#!/usr/bin/python3
"""
new module in square make a function
"""


class Square:
    """
    compute the area of a square
    """

    def __init__(self, size=0):
        """

        :param size: square size to be computed

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        compute the area of a square
        :return: result
        """
        return self.__size * self.__size
