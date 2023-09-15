#!/usr/bin/python3
"""Sudent class Module"""


class Student():
    def __init__(self, first_name, last_name, age):
        """init student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retreives the dictionary representation of the Student instance"""
        if isinstance(attrs, list):
            if len(attrs) == 0:
                return {}
            elif all(isinstance(el, str) for el in attrs):
                return {k: v for (k, v) in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Update instance attributes"""
        for k in json.keys():
            self.k = json[k]
