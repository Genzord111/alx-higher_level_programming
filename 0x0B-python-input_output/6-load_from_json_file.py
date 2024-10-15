#!/usr/bin/python3
import json
"""This modeule contains the load_from_json_file function"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""

    with open(filename, 'r') as file:
        return json.load(file)
