#!/usr/bin/python3
"""check for other types classes"""


def inherits_from(obj, a_class):
    """

    :param obj:to look for his inherited classes
    :param a_class: class that obj belongs to
    :return: boolean
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
