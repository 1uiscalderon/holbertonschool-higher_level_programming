#!/usr/bin/python3
""" inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherates attributes from BaseGeometry"""

    def __init__(self, width, height):
        """Initializing Rectangle Class"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
