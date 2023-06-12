#!/usr/bin/python3
"""Defines a function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class
    or if obj is an instance of a class that inherits
    from a_class
    """
    return isinstance(obj, a_class)
