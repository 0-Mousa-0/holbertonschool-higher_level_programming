#!/usr/bin/python3
"""first module inheritance from other module that i made"""


class MyList(list):
    """class to some functionality"""

    def print_sorted(self):
        """accept list of number then arrange it"""
        ls = list(self)
        print(sorted(ls))
