#!/usr/bin/python3
"""function that creates
an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """creating function using with"""
    with open(filename, "r") as file:
        a = json.load(file)
        return a
