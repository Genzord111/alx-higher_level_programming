#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix[0] == []:
        print('')
    else:

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == (len(matrix[j]) - 1):
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d} ".format(matrix[i][j]), end='')
