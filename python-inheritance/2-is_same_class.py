#!/usr/bin/python3
"""module to check the obj belong to which class"""


def is_same_class(obj, a_class):
    """

    :param obj: to be checked
    :param a_class: that obj belong to?
    :return: boolean
    """
    o = type(obj)
    if o == a_class:
        return True
    else:
        return False
