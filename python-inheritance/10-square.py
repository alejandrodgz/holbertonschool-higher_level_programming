#!/usr/bin/python3
'''this module contains a inherit class form
module 8 and the class is square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class enherited from rectangle
    size is int'''

    def __init__(self, size):
        super().__init__(width=size, height=size)
