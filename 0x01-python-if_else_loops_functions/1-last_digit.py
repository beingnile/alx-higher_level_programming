#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
last = last * -1 if number < 0 else last
string = f"Last digit of {number:d} is {last:}"
if last > 5:
    print(string + " and is greater than 5")
elif last == 0:
    print(string + " and is 0")
elif last < 6 and last != 0:
    print(string + " and is less than 6 and not 0")
