#!/usr/bin/python3
"""creating a class Mylist"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self):
        """constructor de clase"""
        pass

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
