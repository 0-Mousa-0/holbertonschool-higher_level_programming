#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listdiv = []
    for num in my_list:
        if num % 2 == 0:
            listdiv.append(True)
        else:
            listdiv.append(False)

    return listdiv
