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

    def area(self):
        """Area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Prints rectangle using the # symbol"""
        print_rec = ""
        if self.__width == 0 or self.__height == 0:
            return print_rec
        else:
            for i in range(self.__height):
                print_rec += "#" * self.__width + "\n"
            return print_rec[:-1]
