#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """rectanlge class"""

    def __init__(self, width=0, height=0):
        """constructor de clase"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """accediendo a atributo privado"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter and raise errors
        height must be an integer, otherwise raise a TypeError exception
        with the message height must be an integer"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """accediendo a atributo privado"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter and raise errors
        height must be an integer, otherwise raise a
        TypeError exception with the
        message height must be an integer"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("heigth must be an integer")
        if self.__height < 0:
            raise ValueError("heigth must be >= 0")
