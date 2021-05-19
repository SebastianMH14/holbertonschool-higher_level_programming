#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """defines square"""
    def __init__(self, size=0):
        """init class"""
        self.__size = size

    @property
    def size(self):
        """accediendo a size privado"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """init class"""
        if isinstance(size, int) is True:
            self._Square__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """the squere area"""
        return self.__size ** 2

    def print_c(self):
        """print square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
