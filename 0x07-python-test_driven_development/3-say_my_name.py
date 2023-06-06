#!/usr/bin/python3
"""Defines a function that prints the full name"""


def say_my_name(first_name, last_name=""):
    """Prints the full name to stdout"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
