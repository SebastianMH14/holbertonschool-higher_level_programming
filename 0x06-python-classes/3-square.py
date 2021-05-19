#!/usr/bin/python3
"""class square size verification"""


class Square:
    """create a class"""
    def __init__(self, size=0):
        """init class"""
        if isinstance(size, int) is True:
            self._Square__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

def area(self):
    """ the squere area """
    return self._size ** 2
