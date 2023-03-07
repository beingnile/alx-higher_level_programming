#!/usr/bin/python3
for i in range(100):
    if i == 99:
        i = str(i)
        print("{num:s}".format(num=i))
        break

    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
    print("{num:s}".format(num=i), end=', ')
