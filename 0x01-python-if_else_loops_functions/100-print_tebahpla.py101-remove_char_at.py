#!/usr/bin/python3
for i in reversed(range(97, 123)):
    a = chr(i)
    if i % 2 != 0:
        a = (chr(i - 32))
    print("{}".format(a), end='')
