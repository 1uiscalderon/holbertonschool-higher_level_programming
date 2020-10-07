#!/usr/bin/python3
""" Define a Class Student that defines a student"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """ Initializing attibutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
