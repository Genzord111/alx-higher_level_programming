#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    
    while (i < x):
            try:
                try:
                    print("{:d}".format(my_list[i]), end="")
                    i += 1
                    count += 1
                except:
                    i += 1
            except (IndexError):
                pass
    print("")
    return count