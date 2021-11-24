#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = a_dictionary.copy()
    for key in a_dict:
        a_dict[key] *= 2

    return a_dict
