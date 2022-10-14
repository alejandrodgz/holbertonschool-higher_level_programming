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

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
                