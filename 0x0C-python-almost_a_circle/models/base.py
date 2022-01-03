#!/usr/bin/python3

import json
import csv
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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of a JSON string representation.

        Args:
            json_string (str): A str representating a list of dictionaries.

        Returns:
            List represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set.

        Args:
            **dictionary (dict): Key-worded of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                attr = cls(1, 1)
            else:
                attr = cls(1)
        attr.update(**dictionary)
        return attr

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Returns:
            If the file does not exist - an empty list.
            A List of instances.
        """
        json_file = str(cls.__name__) + ".json"
        try:
            with open(json_file, "r") as f:
                objs = Base.from_json_string(f.read())
                return [cls.create(**d) for d in objs]
        except IOError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a list of instances to a csv file.

        Args:
            list_objs (list): A list of inherited instances.
        """
        csv_file = cls.__name__ + ".csv"
        with open(csv_file, "w", newline="") as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                for obj in list_objs:
                    csv.DictWriter(f, fieldnames=attr).writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of instances from a csv file.

        Returns:
            List of classes inheriting from base class.
        """
        csv_file = cls.__name__ + ".csv"
        try:
            with open(csv_file, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=attr)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return "[]"
