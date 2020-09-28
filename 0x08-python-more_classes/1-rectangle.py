#!/usr/bin/python3
"""first class"""


class Rectangle:
    """Class that defines a Rectangle
        - Attributes:
                -width: width of a rectangle
                -height: height of a rectangle
        - Raises:
                -TypeError: If not an int
                -ValueError: If passed a negative number
    """

    def __init__(self, width=0, height=0):
        """instance initializing"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """variable initializing"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """variable initializing"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
