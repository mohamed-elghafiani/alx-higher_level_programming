#!/usr/bin/python3

"""This module contains the implimentation of the function
``print_square(size)``.

Typical usage example:
  print_square(3)
"""


def print_square(size):
    """print_square: prints a square with the character #.

    Args:
      size: An integer representing the square size

    Raises:
      TypeError: If size is of other type than int
      ValueError: If size is <= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
