#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_listc = my_list.copy()
    for i in my_listc:
        if i == search:
            my_listc[my_listc.index(i)] = replace
    return my_listc
