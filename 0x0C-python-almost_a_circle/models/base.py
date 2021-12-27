#!/usr/bin/python3

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
