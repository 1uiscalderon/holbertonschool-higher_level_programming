#!/usr/bin/python3
"""Creating module"""
import json
import csv


class Base:
    """Define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_j = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_j))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 2)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                list_ = cls.from_json_string(f.read())
                objlist = []
                for obj in list_:
                    objlist.append(cls.create(**obj))
                return objlist
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to a csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """save to a csv file"""
        filename = cls.__name__ + ".csv"
        list_ = []
        with open(filename) as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            reader = csv.DictReader(f, fieldnames=fieldnames)
            list_d = {}
            list_d2 = []
            for d in reader:
                for k, v in dict(d).items():
                    list_d[k] = int(v)
                list_d2.append(cls.create(**list_d))
            return list_d2
