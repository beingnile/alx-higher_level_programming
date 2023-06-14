#!/usr/bin/python3
"""Defines a function save_to_json_file()"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file,
    using JSON representation

    Args:
        my_obj(any): An object of any type
        filename(str): The file to write to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
