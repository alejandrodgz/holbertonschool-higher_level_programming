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

    def size(self):
        '''this is a getter'''
        return self.__size

    def size(self, value):
        '''this is a setter for size'''
        self.__size = value

    def area(self):
        '''this is a public method
        to calculate area'''
        area1 = self.__size ** 2
        return area1