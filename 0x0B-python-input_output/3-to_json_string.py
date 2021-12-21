#!/usr/bin/python3

""" Print the json representation of an object """
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj (str): The object.
    Returns:
        The json representation of my_obj.
    """
    return json.dumps(my_obj)
