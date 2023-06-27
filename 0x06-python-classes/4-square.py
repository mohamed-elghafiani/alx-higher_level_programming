#!/usr/bin/python3

"""
    This Module defines the Square class
"""


class Square:
    """
        This class represents a square

    """

    def __init__(self, size=0):
        """
            Initializes an instance of the Square class

            Args:
                size (int, optional): the size of the square. Default to 0.
        """
        self.size = size

    @property
    def size(self):
        """
            Gets the size of the square

            Returns:
                size (int) : the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
            Sets the size of the square

            Args:
                size (int): the size of the square

            Raises:
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
            Calculates the area of the square

            Returns:
                int : The area of the square
        """
        return self.__size ** 2
