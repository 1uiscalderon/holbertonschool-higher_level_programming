#!/usr/bin/python3
""" Define a Class Student that defines a student"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """ Initializing attibutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if type(attrs) is not list:
            return self.__dict__
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
