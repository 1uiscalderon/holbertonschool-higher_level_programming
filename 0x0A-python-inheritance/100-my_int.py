#!/usr/bin/python3
""" Module MyInt"""


class MyInt(int):
    """MyInt class """

    def __init__(self, value):
        """Initializing Square Class"""
        self.__value = value

    def __eq__(self, value):
        return self.__value != value

    def __ne__(self, value):
        return self.__value == value
