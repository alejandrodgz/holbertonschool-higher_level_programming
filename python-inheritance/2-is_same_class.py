#!/usr/bin/python3
'''module 2-is_same_class
it checks if something is an instance
of the class'''


def is_same_class(obj, a_class):
    '''object to analize
    class to watch
    '''
    if isinstance(obj, a_class) and isinstance(obj, a_class) is True:
        return True
    else:
        return False
