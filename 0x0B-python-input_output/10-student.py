#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary of the student object"""
        dict_rep = {}
        if type(attrs) == list:
            for item in attrs:
                if hasattr(self, item):
                    dict_rep[item] = self.__dict__[item]
            return dict_rep
        return self.__dict__
