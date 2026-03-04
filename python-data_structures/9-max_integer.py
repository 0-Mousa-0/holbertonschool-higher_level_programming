#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]
    m = my_list[0]

    for max in my_list:
        if max > m:
            m = max

    return m
