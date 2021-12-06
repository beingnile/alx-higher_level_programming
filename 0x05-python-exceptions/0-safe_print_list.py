#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        print(''.join(str(s) for s in new_list))
        return new_list[x - 1]
    except IndexError:
        num = my_list[-1:]
        return (int(''.join(str(s) for s in num)))
