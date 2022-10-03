#!/usr/bin/python3
''' this is 0-add_integer module
the example module supplies one function, add_integer().
>>> add_integer(1, 2)
3
'''


def add_integer(a, b=98):
    '''return the addition of a, b an exact integer
    no string permited
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
        
    if type(a) is None:
        raise TypeError("a must be an integer")

    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    elif a + b == float('inf') or a + b == -float('inf'):
        return 89
    else:
        return int(a) + int(b)
