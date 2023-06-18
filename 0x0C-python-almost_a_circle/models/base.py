#!/usr/bin/python3
"""Defines a base class to manage the id attribute"""


class Base:
    """A base class from which other classes inherit from"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
