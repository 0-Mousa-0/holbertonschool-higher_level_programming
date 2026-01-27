#!/usr/bin/python3
"""
print square upon the size
"""


class Square:
    """
    print rectangle use property & setter
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        :param size: of rectangle
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """

        :return: area of the rectangle
        """
        return self.__size**2

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

    @property
    def position(self):
        """
        :return: how much spaces
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        :param value: positions
        :return: result to getter
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple")
        if value < 0:
            raise ValueError("position must be >= 0")
        else:
            self.__position = value

    def my_print(self):
        """

        :return:print of rectangle
        """
        if self.__size == 0:
            print()
        if self.__position[0] == 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:

            for i in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size)
