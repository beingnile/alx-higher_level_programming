#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except KeyError:
        return a_dictionary
    finally:
        return a_dictionary
