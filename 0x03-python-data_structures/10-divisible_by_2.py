#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    some_list = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            some_list.append(True)
        else:
            some_list.append(False)

    return some_list
