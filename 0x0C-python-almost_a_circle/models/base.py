#!/usr/bin/python3
"""Class Base private class
attribute __nb_objects = 0
class constructor"""
import json
from os import write


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return list in json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to file
        in json string"""
        if list_objs is None:
            list_objs = []
        dic_t = []
        for a in list_objs:
            dic_t.append(cls.to_dictionary(a))
        with open(cls.__name__ + ".json", "w+") as file:
            file.write(Base.to_json_string(dic_t))

    @staticmethod
    def from_json_string(json_string):
        """add static method"""
        if json_string is None:
            return[]
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """dummy element, method"""
        if cls.__name__ == "Square":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy
