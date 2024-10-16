#!/usr/bin/python3
"""Module contains pascal_triangle function"""


def pascal_triangle(n):
    """Prints a pascal triangle"""

    one = [1, 1]
    my_list = [[1], [1, 1]]
    if n <= 0:
        return []
    elif n == 1:
        return [my_list[0]]
    elif n == 2:
        return my_list

    if n > 2:
        for i in range(n - 2):
            one = [1, 1]
            mid = []
            new_list = my_list[-1]
            i = 0
            while i != len(new_list) - 1:
                mid.append(new_list[i] + new_list[i+1])
                i += 1
            one[1:1] = mid
            my_list.append(one)

    return my_list
