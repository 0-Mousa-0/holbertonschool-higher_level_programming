#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    i = len(newlist)
    if idx <= -1 or idx >= i:
        return my_list
    else:
        newlist[idx] = element
        return newlist
