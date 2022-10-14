#!/usr/bin/python3
"""class student a method
to jsonaize """


class Student:
    """class student bro
    no need to know anymore"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''json method'''
        if attrs is not None:
            dict1 = self.__dict__
            dict2 = {}
            for i in dict1.keys():
                if i in attrs:
                    dict2[i] = dict1[i]
            return dict2
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''aaaa'''
        if json["first_name"] is not None:
            self.first_name = json["first_name"]
        if json["last_name"] is not None:
            self.last_name = json["last_name"]
        if json["age"] is not None:
            self.age = json["age"]
