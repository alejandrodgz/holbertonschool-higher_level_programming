#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    while a < x:
        try:
            print("{}".format(my_list[a]), end="")
            a = a + 1
        except IndexError:
            print("")
            return a
    print("")
    return a
