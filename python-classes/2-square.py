#!/usr/bin/python3
'''
Module square
creating a class with one attribute Size
'''


class Square:
    ''' class with one attribute
    '''

    def __init__(self, size=0):
        '''new attribute
        args:
            size: size of Square'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
