#!/usr/bin/python3
"""all belong to object class"""


def is_kind_of_class(obj, a_class):
    """tell me this obj from which classes"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
