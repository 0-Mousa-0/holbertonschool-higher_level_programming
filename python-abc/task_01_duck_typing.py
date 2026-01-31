#!/usr/bin/python3
"""inheritance for abc class"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """our abc class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """inherit from Shape"""

    def __init__(self, radius=0):
        """

        :param radius:value
        """
        self.radius = radius

    def area(self):
        """

        :return: result
        """
        return math.pi * (self.radius**2)

    def perimeter(self):
        """

        :return: result
        """
        return self.radius * 2 * math.pi


class Rectangle(Shape):
    """inherit from Shape"""

    def __init__(self, width=0, height=0):
        """

        :param width: value
        :param height: value
        """
        self.width = width
        self.height = height

    def area(self):
        """

        :return: result
        """
        return self.width * self.height

    def perimeter(self):
        """

        :return: result
        """
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """

    :param Shape: abc class
    :return: print of infos
    """
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
