#!/usr/bin/python3
"""
Module for basic class implementation
"""


class BaseGeometry:
    """Basic class named BaseGeometry
    """

    def area(self):
        """
        Public instance method: raises exception
        No implementation yet
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method: validate value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
