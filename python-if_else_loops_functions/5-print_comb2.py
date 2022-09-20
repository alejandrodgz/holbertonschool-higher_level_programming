#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print("{0}".format(a))
    else:
        print("{:02d}{} ".format(a, ","), end="")
