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
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
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
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        return self.__x

    @x.setter
    def x(self, x):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        return self.__y

    @y.setter
    def y(self, y):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''just the area of triangle'''

        return self.__height * self.__width

    def display(self):
        '''git the most epical reaction
        '''
        for k in range(self.__y):
            print("")
        for i in range(self.__height):
            print(self.__x * " ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        '''returns everything inside'''
        return ("[Rectangle] ({}) {}/{} - {}/{}" .format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''update values'''
        if len(args) > 0:
            self.id = args[0]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value

        if len(args) > 1:
            self.__width = args[1]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "width":
                    self.__width = value
        if len(args) > 2:
            self.__height = args[2]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
        if len(args) > 3:
            self.__x = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "x":
                    self.__x = value
        if len(args) > 4:
            self.__y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "y":
                    self.__y = value
