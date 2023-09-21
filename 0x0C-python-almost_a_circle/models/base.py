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
        list_dict = cls.to_json_string([list_objs[0].to_dictionary()])
        for obj in list_objs[1:]:
            obj_string = cls.to_json_string([obj.to_dictionary()])[1:]
            list_dict = ",".join([list_dict[:-1], obj_string])
        with open(cls.__name__ + ".json", "w") as file:
            file.write(list_dict)
