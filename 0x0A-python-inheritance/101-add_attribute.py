#!/usr/bin/python3
""" Module MyInt"""


def add_attribute(obj, attribute, value):
    """setting attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
