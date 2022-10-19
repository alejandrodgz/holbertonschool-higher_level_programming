#!/usr/bin/python3
'''this is the class square
that inherits from rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''this is a all new class called square'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''by name again and i say'''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, size):
        super().__init__(size, size)
    
    def update(self, *args, **kwargs):
        
        if len(args) > 0:
            self.id = args[0]
        elif kwargs is not None:
            for key, item in kwargs.items():
                if key == "id":
                    self.id = item
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        elif kwargs is not None:
            for key, item in kwargs.items():
                if key == "size":
                    self.width = item
                    self.height = item
        if len(args) > 2:
            self.x = args[2]
        elif kwargs is not None:
            for key, item in kwargs.items():
                if key == "x":
                    self.x = item
        if len(args) > 3:
            self.y = args[3]
        elif kwargs is not None:
            for key, item in kwargs.items():
                if key == "y":
                    self.x = item
