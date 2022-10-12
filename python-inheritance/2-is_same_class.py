#!/usr/bin/python3
'''module 2-is_same_class 
it checks if something is an instance
of the class'''

def is_same_class(obj, a_class):
    '''object to analize
    class to watch
    '''
    return isinstance(obj, a_class)

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))