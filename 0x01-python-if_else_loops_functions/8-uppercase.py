#!/usr/bin/python3
def uppercase(str):
    cap = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        cap += c
    print("{caps:s}".format(caps=cap))
