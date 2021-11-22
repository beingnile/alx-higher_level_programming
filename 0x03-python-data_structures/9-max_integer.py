#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    large_num = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > large_num:
            large_num = my_list[index]

    return (large_num)
