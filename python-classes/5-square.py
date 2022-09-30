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

    @property
    def size(self):
        '''this is a getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''this is a setter for size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''this is a public method
        to calculate area'''
        area1 = self.__size ** 2
        return area1

    def my_print(self):
        '''print a square of size
        equal to self.__size'''
        if self.__size == 0:
            print("")
        else:
            b = 0
            while b < self.__size:
                a = 0
                while a < self.__size:
                    print("#", end="")
                    a += 1
                print("")
                b += 1
