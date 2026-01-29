#!/usr/bin/python3
"""print rectangle"""


class Rectangle:
    """
    __dict__ called from main

    """

    def __init__(self, width=0, height=0):
        """intilize the width and height of a rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """

        :return: the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value: clc the width
        :return: none
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        :return: the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        :param value: clc the height
        :return: none

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """clc the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """clc the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """first use of join"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            printt = "#" * self.width
        return "\n".join([printt] * self.height)

    def __repr__(self):
        """first use of reper"""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """remove the rectangle"""
        print("Bye rectangle...")
