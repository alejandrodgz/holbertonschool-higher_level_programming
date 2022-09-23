#!/usr/bin/python3
def no_c(my_string):
    a = 0
    for i in my_string:
        if i == 'c' or i == 'C':
            my_string = my_string[:a] + my_string[a + 1:]
            a -= 1
        a += 1
    return my_string
