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
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    
    else:
        return int(a) + int(b)
