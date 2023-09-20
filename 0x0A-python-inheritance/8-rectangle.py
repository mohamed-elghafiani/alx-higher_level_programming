#!/usr/bin/python3
"""Rectangle Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Instance initiator"""
        self.width = super().integer_validator("width", width)
        self.height = super().integer_validator("height", height)
