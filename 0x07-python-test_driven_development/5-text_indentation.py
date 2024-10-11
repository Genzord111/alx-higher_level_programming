#!/usr/bin/python3
"""This module contains a function for string formating"""


def text_indentation(text):
    """Prints text with 2 new lines after each of character: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be string")
    new_str = ""
    size = len(text)
    i = 0

    while(i < size):
        new_str += text[i]
        check = text[i]
        if (check == '.' or check == ':' or check == '?'):
            new_str += '\n'
            j = i + 1

            while text[j] == " ":
                j += 1
            i = j

        else:
            i += 1

    print(new_str)
