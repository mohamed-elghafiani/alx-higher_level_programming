#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Only sub class of"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
