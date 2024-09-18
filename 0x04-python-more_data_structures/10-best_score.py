#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None
    else:
        new_list = []
        for key, value in a_dictionary.items():
            new_list.append((key, value))

        max_num = new_list[0][1]
        name = ""

        for i in new_list:
            if i[1] > max_num:
                max_num = i[1]
                name = i[0]

    return name
