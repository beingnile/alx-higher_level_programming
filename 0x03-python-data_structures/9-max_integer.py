#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    bigint = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > bigint:
            bigint = my_list[index]

    return (bigint)
