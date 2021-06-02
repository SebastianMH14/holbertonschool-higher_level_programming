#!/usr/bin/python3
"""a class Square that inherits
from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """creating a class"""

    def __init__(self, size):
        """constructor de clase"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """obtener el area"""
        return (self.__size * self.__size)

    def __str__(self):
        """Rectangle description: [Rectangle] <width>/<height>"""
        return "[Square] {}/{}".format(self.__size, self.__size)
