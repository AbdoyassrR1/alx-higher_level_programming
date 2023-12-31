#!/usr/bin/python3

"""this module contain Square class"""


class Square:
    """define a Square class"""
    def __init__(self, __size=0) -> None:
        """Intializing the square object with a private size attribute
        Args :
        __size : size of squre
        """
        self.__size = __size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def area(self):
        """ return the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns : size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """propery setter for size
        Args : value
        Raises: Type
        error or value error"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
