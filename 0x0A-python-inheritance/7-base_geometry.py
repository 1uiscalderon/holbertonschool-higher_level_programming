#!/usr/bin/python3
""" Empty class BaseGeometry that defines a BaseGeometry"""


class BaseGeometry:
    """ BaseGeometry class"""
    def area(self):
        """ Error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))
    