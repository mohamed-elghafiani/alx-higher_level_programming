#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """"square instance initiator"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
    
    def __str__(self):
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.__size)
