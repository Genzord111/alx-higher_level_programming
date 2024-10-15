#!/usr/bin/python3
"""This modeule contains the read_file function"""


def append_write(filename="", text=""):
    """Function appends a line of content to filename"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
