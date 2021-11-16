#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastDig = number % 10
elif number < 0:
    lastDig = -(abs(number) % 10)
if lastDig > 5:
    print(f"Last digit of {number} is {lastDig} and is greater than 5")
elif lastDig == 0:
    print(f"Last digit of {number} is {lastDig} and is 0")
elif lastDig < 6:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0")
