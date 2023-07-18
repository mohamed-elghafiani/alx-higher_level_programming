#!/use/bin/python3
"""Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class implimentation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiates an instance of rectangle

        Args:
          width (int): The width of the rectangle
          height (int): The height of the rectangle
          x (int): The x position
          y (int): The y position
          id (int): The instance id

        Attributes:
          width (int): The width of the rectangle
          height (int): The height of the rectangle
          x (int): The x position
          y (int): The y position
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of rectangle's width

        Args:
          value (int): The value of to assign for self.__width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the rectangle's hight
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the rectangle's height

        Args:
          value (int): the value to assign for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the x position of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x position of the rectangle

        Args:
          value (int): The value to assign for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y position of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y position of the rectangle

        Args:
          value (int): The value to assign for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the rectangle's area
        """
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using "#"
        """
        for _ in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """str: Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle
        """
        s1 = "[Rectangle] ({})".format(self.id)
        s2 = "{}/{}".format(self.__x, self.__y)
        s3 = " - {}/{}".format(self.__width, self.__height)
        return s1 + s2 + s3

    def update(self, *args):
        """Update the rectangle instance's public attributes

        Args:
          args: A list of args
        """
        id, width, height, x, y = (None, ) * 5
        if args is not None:
            if len(args) == 1:
                id = args
                super().__init__(id)
            elif len(args) == 2:
                id, width = args
                super().__init__(id)
                self.__width = width

            elif len(args) == 3:
                id, width, height = args
                super().__init__(id)
                self.__width = width
                self.__height = height

            elif len(args) == 4:
                id, width, height, x = args
                super().__init__(id)
                self.__width = width
                self.__height = height
                self.__x = x

            elif len(args) == 5:
                id, width, height, x, y = args
                super().__init__(id)
                self.__width = width
                self.__height = height
