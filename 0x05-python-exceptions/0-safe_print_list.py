#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        for item in new_list:
            print(item, end='')
        print('\n')
        return new_list[x - 1]
    except IndexError:
        num = my_list[-1:]
        return (int(''.join(str(s) for s in num)))
