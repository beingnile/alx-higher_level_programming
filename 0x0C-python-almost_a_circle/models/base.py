#!/usr/bin/python3
"""Defines a base class to manage the id attribute"""
import json


class Base:
    """A base class from which other classes inherit from"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file
        """
        if list_objs is None or len(list_objs) == 0:
            return
        with open(f'{list_objs[0].__class__.__name__}.json', 'w') as f:
            for obj in list_objs:
                f.write(Base.to_json_string([obj.to_dictionary()]))
