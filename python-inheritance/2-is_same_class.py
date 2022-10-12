#!/usr/bin/python3
'''module 2-is_same_class
it checks if something is an instance
of the class'''


def is_same_class(obj, a_class):
    '''object to analize
    class to watch
    '''
    return type(obj) == a_class
