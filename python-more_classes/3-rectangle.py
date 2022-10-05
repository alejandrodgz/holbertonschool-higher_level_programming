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
            raise TypeError('height must be an integer')
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

        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height'''

        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''area of rectangule'''
        return self.__width * self.__height

    def perimeter(self):
        '''area of perimeter'''

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        i = 0
        while i < self.__height:
            j = 0
            while j < self.__width:
                print("#", end="")
                j += 1
            if i != self.__height - 1:
                print("")
            i += 1
        return ""
