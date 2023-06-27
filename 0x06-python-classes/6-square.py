#!/usr/bin/python3

"""
    This Module defines the Square class
"""


class Square:
    """
        This class represents a square

    """

    def __init__(self, size=0, position=(0, 0)):
        """
            Initializes an instance of the Square class

            Args:
                size (int, optional): The size of the square. Default to 0.
                position (tuple, optional) : The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
            Gets the size of the square

            Returns:
                int : The size of the square
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

    @property
    def position(self):
        """
            Gets the postion attribute of the square

            Returns:
                tuple : The position as (x, y)
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
            Sets teh position of the square

            Args:
                position (tuple): The position of the square

            Raises:
                TypeError: If postion isn't a tuple of length 2
        """
        if not isinstance(position, tuple) or (len(position) != 2) or not all(isinstance(num, int) for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
            Calculates the area of the square

            Returns:
                int : The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
            Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()

        for _ in range(self.__size):
            if self.__position[0] > 0:
                print(" "*self.__position[0], end="")
            print("#" * self.__size, end="")
            print()
