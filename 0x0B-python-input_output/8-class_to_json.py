#!/usr/bin/python3
"""Defines a function class_to_json()"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structures(list, dictionary, string, integer and boolean))
    for JSON serialization of an object

    Args:
        obj(any): An object of any type

    Returns:
        (dict): A dictionary mapping of all attributes
    """
    return obj.__dict__
