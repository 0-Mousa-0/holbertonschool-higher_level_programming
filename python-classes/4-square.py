#!/usr/bin/python3
class Square:
    """
    first use of property
    """

    def __init__(self, size=0):
        """
        :param self: need in all methods
        :param size: the value of it
        :return: size amount
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        :return: area amount
        """
        return self.__size * self.__size

    @property
    def size(self):
        """

        :return: size amount
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        :param value: assigned to size
        :return: __size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
