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

        raise Exception("area() is not implemented")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height= height


r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))