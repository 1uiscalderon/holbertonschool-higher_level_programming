#!/usr/bin/python3
"""Returns an object (Python data structure) represented by a JSON string"""
import json


def save_to_json_file(my_obj, filename):
    """json representation of an object"""
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
