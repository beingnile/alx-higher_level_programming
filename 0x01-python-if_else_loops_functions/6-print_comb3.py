#!/usr/bin/python3
someList = []
for i in range(1, 100):
    if i < 10:
        i = '0' + str(i)
    elif i > 10:
        if i % 10 == i // 10:
            continue
    i = str(i)
    if i == '89':
        print("{}".format(i))
        break
    if ''.join(sorted(i)) in someList:
        continue
    else:
        someList += [i]
    print("{}".format(i), end=', ')
