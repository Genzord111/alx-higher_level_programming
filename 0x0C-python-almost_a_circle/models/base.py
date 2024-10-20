#!/usr/bin/python3
"""This module contains the Base class"""
import json


class Base:
    """This is the base class for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id or num of onject"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """returns dictionary of instance attributes as JSON string"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file of Base"""
        atrribute_lists = []
        if list_objs is not None:
           for i in list_objs:
                if isinstance(i, cls):
                    file_name = f"{i.__class__.__name__}.json"
                    atrribute_lists.append(i.to_dictionary())
        
        with open(file_name, 'w') as f:
            json.dump(atrribute_lists, f)
