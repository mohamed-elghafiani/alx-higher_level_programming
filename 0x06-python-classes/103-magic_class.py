#!/usr/bin/python3
import math

"""
    This module defines the MagicClass class
"""


class MagicClass():
    """
        This class represents the MagicClass class
    """
    def __init__(self, radius):
        """
            Instantiate the MagicClass instance

            Args:
                radius (number): The radius of the MagicClass instance
        """
        if not isinstance(radius, int) or not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.radius = radius

    def area(self):
        """
            Calculates the MagicClass instance area
        """
        return math.pi * radius**2

    def circumference(self):
        """
            Claculates the MagicClass instance circumference
        """
        return 2 * math.pi * radius
