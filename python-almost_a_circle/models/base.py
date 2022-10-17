#!/usr/bin/python3
'''this module contains a class
called base'''


class Base:
    '''class private atribute
    called __nb of objects'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
