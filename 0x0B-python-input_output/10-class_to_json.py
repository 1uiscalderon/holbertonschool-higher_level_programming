#!/usr/bin/python3
"""Returns the dictionary description with simple data structure
(list, dict, string, integer and bool) for JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionary description"""
    return obj.__dict__
