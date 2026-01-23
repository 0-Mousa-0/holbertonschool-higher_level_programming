#!/usr/bin/python3
"""
module to divide a matrix elements
by a number
"""
def matrix_divided(matrix, div):
    """

    :param matrix: lists of list ,elements will div by div
    :param div: number that will the division
    :return: matrix divided by div
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div != int(div) and div != float(div):
        raise TypeError("div must be a number")

    r = matrix[0]
    rm = []

    for row in matrix:
        if row != list(row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(r) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        result = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result.append(round(i / div, 2))
        rm.append(result)
        r = row
    return rm


