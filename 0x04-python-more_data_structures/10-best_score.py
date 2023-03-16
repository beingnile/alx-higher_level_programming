#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = sorted(a_dictionary.values())[-1]
    key = [i for i in a_dictionary if a_dictionary[i] == highest]

    return key[0]
