#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """object is exactly an instance of the specified class"""
    return type(obj) is a_class
