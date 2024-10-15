#!/usr/bin/python3
"""This modeule contains the read_file function"""


def write_file(filename="", text=""):
    """Function write single line of content to filename"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
