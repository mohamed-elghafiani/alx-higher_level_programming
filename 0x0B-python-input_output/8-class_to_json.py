#!/usr/bin/python3
"""Convert Class to Json"""

def class_to_json(obj):
    """return the obj representation of a class"""
    return obj.__dict__
