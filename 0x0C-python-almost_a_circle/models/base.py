#!/usr/bin/python3
"""This module contains the Base class"""
import json


class Base:
    """This is the base class for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id value or number of object"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns dictionary of instance attributes as JSON string"""
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        attribute_list = []
        if json_string is not None:
            attribute_list = json.loads(json_string)
        return attribute_list

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        atrribute_lists = []
        if list_objs is not None:
            for i in list_objs:
                if isinstance(i, cls):
                    file_name = f"{i.__class__.__name__}.json"
                    atrribute_lists.append(i.to_dictionary())

        with open(file_name, 'w') as f:
            json.dump(atrribute_lists, f)

    @classmethod
    def create(cls, **dictionary):
        container_class = cls(1, 1, 1)
        container_class.update(**dictionary)
        return container_class

    @classmethod
    def load_from_file(cls):
        class_list = []
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, 'r') as f:
                class_list = json.load(f)
        except IOError:
            pass

        return class_list
