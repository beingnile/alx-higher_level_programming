#!/usr/bin/python3

""" Add attributes to object """


def add_attribute(obj, name, value):
    """
    Args:
        obj : The object.
        name (str): Attribute name.
        value : Attribute value.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
