#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = my_list[:]

    if idx < 0 or idx >= len(new_list):
        return new_list
    else:
        my_list.clear()
        for i in new_list:
            if i == new_list[idx]:
                continue
            else:
                my_list.append(i)
    return my_list
