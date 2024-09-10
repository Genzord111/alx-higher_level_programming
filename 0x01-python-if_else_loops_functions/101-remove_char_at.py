#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    stop = 0

    for i in str:
        if stop != n:
            copy = copy + i
            stop = stop + 1
        else:
            copy = copy
            stop = stop + 1
    return copy
