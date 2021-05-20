#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """rectanlge class"""
    def __init__(self, width=0, height=0):
        """constructor de clase"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ accediendo a atributo privado"""
        return self.__height

    @property
    def width(self):
        """accediendo a atributo privado"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if isinstance(value, int) is True:
            self._Rectangle__width = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @height.setter
    def height(self, value):
        """height setter"""
        if isinstance(value, int) is True:
            self._Rectangle__height = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """metodo de clase"""
        return (self.__width * self.__height)

    def perimeter(self):
        """metodo de clase"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
