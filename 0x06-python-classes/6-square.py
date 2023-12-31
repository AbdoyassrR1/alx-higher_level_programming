#!/usr/bin/python3
"""    This script defines a basic Square class."""


class Square:
    """
    Define a class named Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Intializing the square object with a private size attribute"""
        self.position = position
        self.size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A public instance method to calculate area of square
        Returns : square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns : size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """propery setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """a method to access postition"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
            len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
