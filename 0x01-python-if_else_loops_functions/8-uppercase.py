#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = i
        if (ord(a) < 128 and ord(a) > 96):
            a = chr(ord(a)-32)
        print("{}".format(a), end='')
    print('')
