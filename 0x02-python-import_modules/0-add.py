#!/usr/bin/python3
from add_0 import add
a = 1
b = 2
res = add(a, b)
if __name__ == "__main__":
    print("{a:d} + {b:d} = {res:d}".format(a=a, b=b, res=res))
