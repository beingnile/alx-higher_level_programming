#!/usr/bin/python3
"""Defines a function from_json_string()"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string

    Args:
        my_str(str): A JSON str

    Returns:
        (any): An object of any type, depending on the JSON str
    """
    return json.loads(my_str)
