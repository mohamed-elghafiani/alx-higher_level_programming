#!/usr/bin/python3
"""Sudent class Module"""


class Student():
    def __init__(self, first_name, last_name, age):
        """init student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retreives the dictionary representation of the Student instance"""
        return self.__dict__
