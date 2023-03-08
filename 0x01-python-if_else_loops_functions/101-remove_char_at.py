#!/usr/bin/python3
def remove_char_at(str, n):
    myList = list(str)
    if n >= 0:
        try:
            removed = myList.pop(n)
        except IndexError:
            result = ''.join(myList)
    result = ''.join(myList)
    return result
