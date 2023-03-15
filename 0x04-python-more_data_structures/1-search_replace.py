#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    if len(new_list) > 0:
        for i in range(len(new_list)):
            if new_list[i] == search:
                new_list[i] = replace

    return new_list
