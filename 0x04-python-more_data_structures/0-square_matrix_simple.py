#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    squared = []
    for i in matrix:
        squared.append([x**2 for x in i])

    return squared
