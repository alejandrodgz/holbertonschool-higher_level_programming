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
