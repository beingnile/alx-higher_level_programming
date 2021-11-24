#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is dict:
        return None

    retval = list(a_dictionary.keys())[0]
    bigval = a_dictionary[retval]
    for k, v in a_dictionary.items():
        if v > big:
            bigval = v
            retval = k
    return retval
