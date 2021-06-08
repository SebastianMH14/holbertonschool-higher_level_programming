#!/usr/bin/python3
"""the class Rectangle
that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """creating a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor de clase"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """accediendo a atributo privado"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) == int:
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """accediendo a atributo privado"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """accediendo a atributo privado"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) == int:
            self.__x = value
        else:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """accediendo a atributo privado"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) == int:
            self.__y = value
        else:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """adding metod"""
        return (self.__width * self.__height)

    def display(self):
        """adding display metod"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            print()
