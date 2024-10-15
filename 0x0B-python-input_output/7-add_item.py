#!/usr/bin/python3
"""This module contains a function to add arguments to a json"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(arg):
    """This retrievs a json list and appends anew item"""
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
        save_to_json_file(my_list, "add_item.json")

    for i in range(1, len(arg)):
        my_list.append(arg[i])

    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_item(sys.argv)
