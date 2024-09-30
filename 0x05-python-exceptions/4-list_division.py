#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    count = 0
    i = 0
    j = 0

    while count < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[j])
        except IndexError:
            print("out of range")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)

        i += 1
        j += 1
        count += 1

    return new_list
