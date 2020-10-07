#!/usr/bin/python3
"""Returns an object (Python data structure) represented by a JSON string"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename) as a_file:
        return json.load(a_file)
