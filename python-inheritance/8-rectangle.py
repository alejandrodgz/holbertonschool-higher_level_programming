#!/usr/bin/python3
""" module 7-base_geometry
with class BaseGeometry
an area method"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''new class
    '''

    def __init__(self, width, height):
        '''new method'''

        self.integer_validator('width', width)
        self.__width = width

        self.integer_validator('height', height)
        self.__height = height
