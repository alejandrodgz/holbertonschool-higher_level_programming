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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if a is None:
        raise TypeError("a must be an integer")

    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
    #a + b == float('inf') or a + b == -float('inf'):
    #    return 89
        