#!/usr/bin/python3
"""This module contains a matrix divider function"""


def matrix_divided(matrix, div):
    """Returns new matrix with all element divided by div"""
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if (len(matrix) < 2) or not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

        elif (len(matrix[0]) != len(i)):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(el / div, 2) for el in row] for row in matrix]
