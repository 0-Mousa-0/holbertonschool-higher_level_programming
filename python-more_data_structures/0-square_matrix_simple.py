#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squMat = []
    for row in matrix:
        newrow = []
        for i in row:
            newrow.append(i**2)
        squMat.append(newrow)

    return squMat
