#!/usr/bin/python3
'''module 3-is_kind_of_class
it checks if something is an instance
of the class'''


def inherits_from(obj, a_class):
    '''object to analize
    class to watch
    '''
    return (type(obj) is not a_class and issubclass(obj, a_class))
