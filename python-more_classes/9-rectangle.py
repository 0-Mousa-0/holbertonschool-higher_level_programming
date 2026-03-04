#!/usr/bin/python3
"""print rectangle"""


class Rectangle:
    """
    __dict__ called from main

    """

    number_of_instances = 0
    print_symbol = "#"
    bigger_or_equal = 0

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
        Rectangle.number_of_instances += 1

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
            printt = str(self.print_symbol) * self.width

            printt = "#" * self.width
        return "\n".join([printt] * self.height)

    def __repr__(self):
        """first use of reper"""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """remove the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """comparing between two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.width > rect_2.width:
            bigger_or_equal = rect_1
            return bigger_or_equal
        elif rect_1.width < rect_2.width:
            bigger_or_equal = rect_2
            return bigger_or_equal

    @classmethod
    def square(cls, size=0):
<<<<<<< HEAD
        """cls the square of the rectangle"""
=======
        """clc the square of the rectangle"""
>>>>>>> a2fdb4a9e5f570e213b2dbac71c444e23b324593

        return cls(size, size)
