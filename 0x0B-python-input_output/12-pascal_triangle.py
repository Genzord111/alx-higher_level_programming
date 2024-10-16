#!/usr/bin/python3
"""Module contains pascal_triangle function"""


def pascal_triangle(n):
    """returns a pascal triangle"""

    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(1, n):
        prev_row = my_list[-1]
        new_row = [1]  # Start each row with 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)  # End each row with 1
            my_list.append(new_row)

    return my_list
