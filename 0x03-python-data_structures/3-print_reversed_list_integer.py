#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    if len(my_list) > 0:
        new_list = my_list[-1::-1]
        for i in new_list:
            print("{:d}".format(i))
