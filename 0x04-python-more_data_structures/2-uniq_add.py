#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    full_sum = 0
    for i in my_set:
        full_sum += i

    return full_sum
