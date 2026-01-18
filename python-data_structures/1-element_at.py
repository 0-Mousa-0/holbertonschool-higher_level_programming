#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    if idx <= -1 or idx >= i:
        return None
    else:
        return my_list[idx]
