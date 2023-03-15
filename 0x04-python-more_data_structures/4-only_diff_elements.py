#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    for i in set_2:
        if i in set_1:
            set_1.remove(i)
            continue
        set_1.add(i)

    return set_1
