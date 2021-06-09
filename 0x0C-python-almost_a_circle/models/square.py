#!/usr/bin/python3
"""he class Square that
inherits from Rectangle"""


from typing import Sized
from models.rectangle import Rectangle


class Square(Rectangle):
    """creating class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor of class with init super class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """accediendo a atributo privado"""
        return self.width

    @size.setter
    def size(self, value):
        """width setter"""
        if type(value) == int:
            self.height = value
            self.width = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.__x, self.__y, self.__width)





