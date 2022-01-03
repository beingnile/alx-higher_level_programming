#!/usr/bin/python3

import json
"""This module defines a base class for other classes"""


class Base:
    """The Base for all the other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class

        Attributes:
            id (int): The ID
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            The json representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json representation of list_objs to a file

        Args:
            list_objs (list): List of instances that inherit from base class
        """
        json_file = cls.__name__ + ".json"
        with open(json_file, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(obj_dicts))
