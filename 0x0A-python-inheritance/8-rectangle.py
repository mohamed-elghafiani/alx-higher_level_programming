#!/usr/bin/python3
"""Rectangle Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Instance initiator"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
