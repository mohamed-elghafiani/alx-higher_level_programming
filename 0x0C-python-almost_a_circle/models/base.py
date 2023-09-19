#!/usr/bin/python3
"""Base class module
"""


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
