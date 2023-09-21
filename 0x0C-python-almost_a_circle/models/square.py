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
        """Return the string representation of the Square instance"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.__size)

    def update(self, *args, **kwargs):
        """Update instance's attributes"""
        super().update(*args, **kwargs)
        if args is not None:
            if len(args) == 1:
                id = args[0]
                super().update(id)

            elif len(args) == 2:
                id, size = args
                self.__size = size
                super().update(id, size, size)

            elif len(args) == 3:
                id, size, x = args
                super().update(id, size, size, x)

            elif len(args) == 4:
                id, size, x, y = args
                super().update(id, size, size, x, y)

        if kwargs is not None:
            if kwargs.get("size", None):
                self.__size = kwargs["size"]
