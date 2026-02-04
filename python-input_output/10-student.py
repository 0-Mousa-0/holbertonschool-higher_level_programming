#!/usr/bin/python3
"""save the object elements"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ "assign the attributes values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """python object in dictionary format"""
        if attrs is None:
            return self.__dict__
        else:
            newDict = {}
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    newDict[attr] = self.__dict__[attr]

            return newDict
