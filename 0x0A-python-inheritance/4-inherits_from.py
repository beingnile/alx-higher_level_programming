#!/usr/bin/python3
"""Defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that
    inherited from the specified class
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
