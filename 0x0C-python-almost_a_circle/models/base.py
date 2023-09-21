#!/usr/bin/python3
"""Base class module
"""
import json


class Base():
    """Base class implimentation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiate base class instance"""
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return str("[]")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        if list_objs:
            list_dict = cls.to_json_string([list_objs[0].to_dictionary()])
            for obj in list_objs[1:]:
                obj_string = cls.to_json_string([obj.to_dictionary()])[1:]
                list_dict = ",".join([list_dict[:-1], obj_string])
        else:
            list_dict = "[]"
        with open(cls.__name__ + ".json", "w") as file:
            file.write(list_dict)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from .json file"""
        try:
            objs = []
            with open(cls.__name__ + ".json") as file:
                objs = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        for i, obj_dict in enumerate(objs):
            objs[i] = cls.create(**obj_dict)

        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list_objs to CSV file"""
        if not list_objs:
            with open(cls.__name__ + ".csv", "x"):
                return

        with open(cls.__name__ + ".csv", "w") as file:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                file.write(",".join(map(str, obj_dict.values())) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Loads objs from CSV file"""
        filename = cls.__name__
        objs = []
        try:
            with open(filename + ".csv") as file:
                objs_list = []
                for obj in file.read():
                    objs_list.append(list(map(int, obj.split(","))))
                objs_dict = []
                for obj in objs_list:
                    obj_dict = {}
                    obj_dict["id"] = obj[0]
                    if filename == "Rectangle":
                        obj_dict["width"] = obj[1]
                        obj_dict["height"] = obj[2]
                        obj_dict["x"] = obj[3]
                        obj_dict["y"] = obj[4]
                    if filename == "Square":
                        obj_dict["size"] = obj[1]
                        obj_dict["x"] = obj[2]
                        obj_dict["y"] = obj[3]

                    objs_dict.append(obj_dict)

                for i, obj_dict in enumerate(objs_dict):
                    objs.append(cls.create(**obj_dict))

        except FileNotFoundError:
            return []

        return objs
