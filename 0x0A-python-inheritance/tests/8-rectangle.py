#!/usr/bin/python3
"""
Module for class that inherits from BaseGeometry
"""

"""Parent class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Basic class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
