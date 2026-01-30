#!/usr/bin/python3
"""area module"""


class BaseGeometry:
    """clc area class"""

    def area(self):
        """

        :return:Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        :param name:string
        :param value: number
        :return: its can be an inputs or not
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
