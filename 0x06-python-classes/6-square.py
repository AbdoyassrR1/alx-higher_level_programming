#!/usr/bin/python3

"""this module contain Square class"""


class Square:
    """define a Square class"""
    def __init__(self, __size=0, __position=(0, 0)) -> None:
        """Intializing the square object with a private size attribute
        Args :
        __size : size of squre
        """
        self.__size = __size
        self.positon = __position
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

    @property
    def position(self):
        """method to access position"""
        return self.__position

    @position.setter
    def positon(self, value):
        """method to set the position"""
        if type(value) is not tuple or len(value) is not 2 or \
                type(value[0]) is not int or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
