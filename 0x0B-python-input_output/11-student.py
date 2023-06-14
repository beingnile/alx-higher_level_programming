#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary rep of object"""
        dict_rep = {}
        if type(attrs) == list:
            for items in attrs:
                if hasattr(self, item):
                    dict_rep[item] = self.__dict__[item]
            return dict_rep
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
