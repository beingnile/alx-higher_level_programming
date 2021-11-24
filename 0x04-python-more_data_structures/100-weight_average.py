#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is list:
        return 0
    avg = 0
    total = 0
    for tuples in my_list:
        avg += (tuples[0] * tuples[1])
        total += tuples[1]

    weight = avg / total
    return weight
