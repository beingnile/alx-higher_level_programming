#!/usr/bin/python3
def no_c(my_string):
    the_string = list(my_string)
    for item in the_string:
        if item == 'c' or item == 'C':
            the_string.remove(item)
    the_string = ''.join([str(item) for item in the_string])
    return the_string
