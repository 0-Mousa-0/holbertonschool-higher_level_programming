#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list1 = my_list[:x]
        i = 0
        for item in my_list1:
            print("{:d}".format(item), end="")
            i = i + 1
        print()
        return i
    except IndexError:
        print("something went wrong")
