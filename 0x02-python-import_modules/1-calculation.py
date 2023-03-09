#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    res = add(a, b)
    print("{a:d} + {b:d} = {res:d}".format(a=a, b=b, res=res))
    res = sub(a, b)
    print("{a:d} - {b:d} = {res:d}".format(a=a, b=b, res=res))
    res = mul(a, b)
    print("{a:d} * {b:d} = {res:d}".format(a=a, b=b, res=res))
    res = div(a, b)
    print("{a:d} / {b:d} = {res:d}".format(a=a, b=b, res=res))
