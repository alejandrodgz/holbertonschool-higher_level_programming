#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print("{0}".format(a))
    else:
        if a < 10:
            print("{0}{1}{2} ".format(a // 10, a, ","), end="")
        else:
            print("{0}{1} ".format(a, ","), end="")
