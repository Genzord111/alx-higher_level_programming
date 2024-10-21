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
        if list_dictionaries is not None and list_dictionaries != {}:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """converts a json string to its python equivalent and stores
        it in a list"""
        attribute_list = []
        if json_string is not None:
            attribute_list = json.loads(json_string)
        return attribute_list

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a
        file of 'classname.json"""
        atrribute_lists = []
        file_name = f"{cls.__name__}.json"

        if list_objs is not None and isinstance(list_objs, list):
            for instance in list_objs:
                if isinstance(instance, cls):
                    atrribute_lists.append(instance.to_dictionary())

        with open(file_name, 'w') as f:
            json.dump(json.loads(cls.to_json_string(atrribute_lists)), f)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        container_class = cls(1, 1)
        container_class.update(**dictionary)
        return container_class

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file created
        using the save_to_file method"""
        class_list = []
        file_name = f"{cls.__name__}.json"
        print(file_name)
        try:
            with open(file_name, 'r') as f:
                for ele in cls.from_json_string(json.load(f)):
                    class_list.append(cls.create(**ele))
        except IOError:
            pass
        return class_list
