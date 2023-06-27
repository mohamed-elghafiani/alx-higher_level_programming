#!/usr/bin/python3

"""
    This Module defines the Square class
"""


class Square:
    """
        This class represents a square

        Methods:
       
    """

    def __init__(self, size=0):
        """
            Initializes an instance of the Square class

            args:
                size(int, optional): the size of the square. Default to 0.

            raises:
                TypeError: If size is not an integer
                ValueError: If size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            This method returns the current square area
        """
        return self.__size ** 2
