#!/usr/bin/python3
'''this module contains a class
called base'''

import json
import sys

from holbertonschool-higher_level_programming.python-input_output.3-to_json_string import to_json_string

class Base:
    '''class private atribute
    called __nb of objects'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''class inherited from Base
    called Rectangle that stores, ahmm..
    a rectangle'''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """method to convert to json string"""
        if list_dictionaries is None:
            list1 = "[]"
            return list1
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save a class object'''
        if list_objs is None:
            list1 = []
            return list1
        with open((cls.__name__, ".json"), mode = "w+", encoding = "utf-8") as f:
            f.write(to_json_string(list_objs))      
