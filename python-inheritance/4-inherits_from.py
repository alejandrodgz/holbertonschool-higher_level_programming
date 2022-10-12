#!/usr/bin/python3
'''module 3-is_kind_of_class
it checks if something is an instance
of the class'''

def inherits_from(obj, a_class):
    '''object to analize
    class to watch
    '''
    return type(obj) is not a_class and isinstance(obj, a_class)
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))