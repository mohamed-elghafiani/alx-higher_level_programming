#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """"square instance initiator"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.__x, self.__y, self.__size)
