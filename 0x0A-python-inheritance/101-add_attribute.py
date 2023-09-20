#!/usr/bin/python3
"""add_attribute Module"""


def add_attribute(obj, name, value):
    """add attribute to obj if possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
