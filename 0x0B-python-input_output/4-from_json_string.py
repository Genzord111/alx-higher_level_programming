#!/usr/bin/python3
"""This modeule contains the t0_json_string function"""


import json


def from_json_string(my_str):
    """returns the JSON representation of an object (python data structure)"""

    return json.loads(my_str)
