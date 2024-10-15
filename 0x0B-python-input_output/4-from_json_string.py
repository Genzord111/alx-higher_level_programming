#!/usr/bin/python3
import json
"""This modeule contains the t0_json_string function"""


def from_json_string(my_str):
    """returns the JSON representation of an object (python data structure)"""

    return json.loads(my_str)
