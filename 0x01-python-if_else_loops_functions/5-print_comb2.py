#!/usr/bin/python3
for decimal in range(00, 100):
    if decimal == 99:
        print("{}".format(decimal), end='\n')
    print("{:02}".format(decimal), end=', ')
