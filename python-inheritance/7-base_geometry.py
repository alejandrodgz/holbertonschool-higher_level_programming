#!/usr/bin/python3
""" module 7-base_geometry
with class BaseGeometry
an area method"""

class BaseGeometry:
    """this is an empty class"""

    def integer_validator(self, name, value):
        """validator of integer method
        name: name of the variable
        value: value related to name"""

        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.value = value

    def area(self):
        """method not implemented"""
