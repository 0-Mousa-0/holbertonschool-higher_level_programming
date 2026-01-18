#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for i, num in enumerate(row):
            if not num:
                print("")
            print("{:d}".format(num), end=" ")
            i += 1
        print()
