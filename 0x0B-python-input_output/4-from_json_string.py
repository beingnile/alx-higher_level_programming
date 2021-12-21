#!/usr/bin/python3

""" Returns an object represented by a JSON string """
import json


def from_json_string(my_str):
    """
    Args:
        my_str (str): The JSON string
    Returns:
        The object string
    """
    return json.loads(my_str)
