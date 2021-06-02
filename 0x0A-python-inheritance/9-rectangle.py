#!/usr/bin/python3
"""Write a class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creating a class"""

    def __init__(self, width, height):
        """constructor de clase"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("heigth", self.__height)

    def area(self):
        """obtener area"""
        return self.__width * self.__heigth

    def __str__(self):
        """Rectangle description: [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
