#!/usr/bin/python3
"""
diffrent module same name
"""


class Square:
    """
    parameter have init value 0, private attribute,
    raise the error when its happen
    """

    def __init__(self, size=0):
        """

        :param size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self._Square__size = size
