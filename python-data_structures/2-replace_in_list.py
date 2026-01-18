#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = len(my_list)
    if idx <= -1 or idx >= i:
        return my_list
    else:
        my_list[idx] = element
        return my_list
