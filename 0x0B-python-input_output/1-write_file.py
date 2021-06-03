#!/usr/bin/python3
"""writes a string to a text file
(UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """use the with statement"""
    with open(filename, 'w', encoding="utf-8") as file:
        a = file.write(text)
        return a
