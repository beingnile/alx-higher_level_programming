#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]

    my_list[-1] = None

    my_list.remove(None)

    return my_list
