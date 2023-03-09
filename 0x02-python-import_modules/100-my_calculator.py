#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = str(argv[2])
    a = int(argv[1])
    b = int(argv[3])
    if op == "+":
        res = add(a, b)
        print(f"{a} + {b} = {res}")
    elif op == "-":
        res = sub(a, b)
        print(f"{a} - {b} = {res}")
    elif op == "*":
        res = mul(a, b)
        print(f"{a} * {b} = {res}")
    elif op == "/":
        res = div(a, b)
        print(f"{a} / {b} = {res}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
