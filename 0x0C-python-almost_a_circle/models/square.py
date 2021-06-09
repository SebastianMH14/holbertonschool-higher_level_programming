#!/usr/bin/python3
"""he class Square that
inherits from Rectangle"""


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
            self.width = value
            self.height = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update metod with args"""
        n = len(args)
        if n > 0:
            for i in range(n):
                if i == 0:
                    setattr(self, "id", args[0])
                if i == 1:
                    setattr(self, "size", args[1])
                if i == 2:
                    setattr(self, "x", args[2])
                if i == 3:
                    setattr(self, "y", args[3])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
