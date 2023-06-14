#!/usr/bin/python3
"""Defines a function load_from_json_file()"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename(str): The JSON file

    Returns:
        (any): An object of any type depending on the JSON file
    """
    with open(filename, 'r') as f:
        obj = json.load(f)

    return obj
