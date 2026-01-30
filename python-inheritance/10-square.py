#!/usr/bin/python3
"""import from rectangle now"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """find the size from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
