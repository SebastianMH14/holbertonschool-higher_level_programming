#!/usr/bin/python3
"""Class Base private class
attribute __nb_objects = 0
class constructor"""

class Base:
    """creando la clase"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor de clase"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
