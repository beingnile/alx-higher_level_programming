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
