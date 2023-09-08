#!/usr/bin/python3

"""
    This module defines the aadd_integer function
"""


def add_integer(a, b=98):
    """Calculates the value of a + b

    Args:
      a: An integer or float
      b: An integer or float

    Raises:
      TypeError: If either a or b aren't integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
