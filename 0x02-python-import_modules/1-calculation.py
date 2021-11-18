#!/usr/bin/python3
import calculator_1.py as calc

a = 10
b = 5

if __name__ == '__main__':
    print("{:d} + {:d} = {:d}".format(calc.add(a, b)))
    print("{:d} + {:d} = {:d}".format(calc.sub(a, b)))
    print("{:d} + {:d} = {:d}".format(calc.mul(a, b)))
    print("{:d} + {:d} = {:d}".format(calc.div(a, b)))
