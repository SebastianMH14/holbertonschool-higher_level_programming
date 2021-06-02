#!/usr/bin/python3
"""Write a class BaseGeometry"""


class BaseGeometry:
    """creating a class"""

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
