#!/usr/bin/python3
"""is kind of a class"""


def is_kind_of_class(obj, a_class):
    """return if obj is instance of a_class"""
    return issubclass(type(obj), a_class)
