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
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update metod with args"""
        n = len(args)
        if n > 0:
            for i in range(n):
                if i == 0:
                    setattr(self, "id", args[0])
                if i == 1:
                    setattr(self, "width", args[1])
                if i == 2:
                    setattr(self, "height", args[2])
                if i == 3:
                    setattr(self, "x", args[3])
                if i == 4:
                    setattr(self, "y", args[4])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """adding metod"""
        dic_t = {}
        for k in self.__dict__:
            k_n = k.replace("_Rctangle_", "")
            dic_t[k_n] = self.__dict__[k]
        return dic_t
