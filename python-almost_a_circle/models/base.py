#!/usr/bin/python3
'''this module contains a class
called base'''

from genericpath import isfile
import os.path
import json
from venv import create


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

        list1 = []
        if list_objs is not None:
            for i in list_objs:
                list1.append(cls.to_dictionary(i))

        extension = cls.__name__ + ".json"
        with open(extension, mode="w+", encoding="utf-8") as f:
            f.write(cls.to_json_string(list1))

    @staticmethod
    def from_json_string(json_string):
        list1 = []
        if json_string is None:
            return list1
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename) is False:
            list1 = []
            return list1

        list1 = []
        with open(filename, mode="r+", encoding="utf-8") as f:
            string1 = f.read()
            a = cls.from_json_string(string1)
            for i in a:
                list1.append(cls.create(**i))

            return list1
