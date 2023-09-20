#!/usr/bin/python3
"""Square Module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """instnace initiator"""
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the instance area"""
        return self.__size ** 2

    def __str__(self):
        return super().__str__()
