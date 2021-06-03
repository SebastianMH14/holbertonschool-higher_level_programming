#!/usr/bin/python3
"""class Student that
defines a student"""


class Student:
    """creating a class"""

    def __init__(self, first_name, last_name, age):
        """class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary
        representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            aux = {}

            for i in attrs:
                if i in self.__dict__:
                    aux[i] = self.__dict__[i]

            return aux
