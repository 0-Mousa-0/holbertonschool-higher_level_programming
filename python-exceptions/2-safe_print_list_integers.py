#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    listint = my_list
    i = 0
    for item in range(x):
        try:
            print("{:d}".format(listint[item]), end="")
            i += 1
        except (TypeError, ValueError):
            pass
    print()
    return i
