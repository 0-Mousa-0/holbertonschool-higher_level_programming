#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.items(), key=lambda item: item[0])
    i = 0
    for item in sorted_dictionary:
        print(item[0] + ": " + str(item[1]))
