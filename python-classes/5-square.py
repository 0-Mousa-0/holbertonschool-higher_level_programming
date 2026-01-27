#!/usr/bin/python3
"""
print square upon the size
"""


class Square:
    """print rectangle use property & setter"""
    def __init__(self, size=0):
        """
        :param size: of rectangle
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        :return: the setted size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        :param value: SIZE SET
        :return: NONE
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """

        :return: area of the rectangle
        """
        return self.__size**2

    def my_print(self):
        """

        :return:print of rectangle
        """
        if self.__size == 0:
            print("\n")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
