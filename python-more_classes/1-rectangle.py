#!/usr/bin/python3
'''
module 0-rectangule
contain class Rectangule
nothing done
'''


class Rectangle:
    '''class Rectagule
    width must be an integer
    height must be an integer
    '''

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if isinstance(height, int) is False:
            self.__height = height
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        '''getter for width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''

        self.__width = value

    @property
    def height(self):
        '''getter for height'''

        return self.__height

    @width.setter
    def height(self, value):
        '''setter for height'''

        self.__height = value
