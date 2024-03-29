#!/usr/bin/python3
"""Defines a function to_json_string()"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj(any): An object of any type

    Return:
        (str): The JSON representation of an object
    """
    return json.dumps(my_obj)
