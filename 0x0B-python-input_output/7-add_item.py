#!/usr/bin/python3
"""This module contains a function to add arguments to a json"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys

def add_item(arg):
    my_list = load_from_json_file("add_item.json")

if __name__ == "__main__":
    add_item(sys.argv)
