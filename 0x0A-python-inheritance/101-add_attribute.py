#!/usr/bin/python3
"""Defines a function add_attribute()"""


def add_attribute(*args):
    """Tries to add a new attribute to an object"""
    if not hasattr(args[0], "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(args[0], args[1], args[2])
