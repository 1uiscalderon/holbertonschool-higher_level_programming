#!/usr/bin/python3
""" Empty class Square that defines a square
    Attributes:
        size type int: size of the square
    """


class Square:
    """Square as a Class"""
    def __init__(self, size=0):
        """Initialization of attributes"""
        self.__size = size

    def area(self):
        """defines area of the Square"""
        return self.__size ** 2

    @property
    def size(self):
        """Defines size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines size of Square with a value entered"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
