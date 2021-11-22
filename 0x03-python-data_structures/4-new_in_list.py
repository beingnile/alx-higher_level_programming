#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy = my_list.copy()
    if idx < 0:
        return my_copy
    elif idx > (len(my_list) - 1):
        return my_copy
    else:
        my_copy[idx] = element
        return my_copy
