#!/usr/bin/python3
"""Write a class Rectangle
that inherits from BaseGeometry
(7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creating a class Rectangle
    heredada from basegeometry"""

    def __init__(self, width, height):
        """constructor de clase
        instantiation with width and height"""
        self.__width = width
        self.__heigth = height
        self.integer_validator("width", self.__width)
        self.integer_validator("heigth", self.__heigth)
