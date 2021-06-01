#!/usr/bin/python3
"""Write a class Rectangle"""

class BaseGeometry:
    """creating a class"""

    def __init__(self):
        """creating constructor"""
        pass

    def area(self):
        """raises an Exception with the
        message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



class Rectangle(BaseGeometry):
    """creating a class"""


    def __init__(self, width, height):
        self.__width= width
        self.__heigth = height

    def width(self, width, heigth):
        myrectangle.integer_validator(width, heigth)
myrectangle = Rectangle('width', 'height')

