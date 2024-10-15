#!/usr/bin/python3
"""This modeule contains the read_file function"""


def read_file(filename=""):
    """Function reads the content of filename"""

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
