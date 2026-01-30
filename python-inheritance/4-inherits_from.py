#!/usr/bin/python3
"""check for other types classes"""


def inherits_from(obj, a_class):
    """look for another form of inheritance"""
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    else:
        return False
