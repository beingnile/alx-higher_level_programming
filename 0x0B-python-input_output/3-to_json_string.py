#!/usr/bin/python3
import json
""" Print the json representation of an object """


def to_json_string(my_obj):
    """
    Args:
        my_obj (str): The object.
    Returns:
        The json representation of my_obj.
    """
    jdump = json.dumps(my_obj)
    return jdump
