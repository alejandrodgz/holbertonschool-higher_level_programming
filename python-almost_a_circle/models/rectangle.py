#!/usr/bin/python3
'''this module contains a class
called base'''

from models.base import Base

'''import module is necessary'''


class Rectangle(Base):
    '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        self.__width = value

    @property
    def height(self):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        self.__height = value

    @property
    def x(self):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        self.__x = value

    @property
    def y(self):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        self.__y = value
