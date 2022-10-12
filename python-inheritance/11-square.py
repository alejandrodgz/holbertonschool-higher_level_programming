#!/usr/bin/python3
'''this module contains a inherit class form
module 8 and the class is square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class enherited from rectangle
    size is int'''

    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(width=size, height=size)
        self.__size = size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
