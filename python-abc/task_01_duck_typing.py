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
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return self.radius * 2 * math.pi


class Rectangle(Shape):
    """inherit from Shape"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(Shape):
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
