#!/usr/bin/python3

"""Return the JSON representation of an object (string)
"""
import json


def load_from_json_file(filename):
    """returns the JSON representation of an object (string)
    """
    with open(filename) as f:
        data = json.load(f)
    return data
