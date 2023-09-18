#!/usr/bin/python3

from modles.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """calc the area of rectangle"""
        return self.height * self.width

    def display(self):
        """display rectangle with "#"
        Returns:
        print "#" according to w and h_
        """
        for y_val in range(self.__y):
            print()

        for i in range(self.__height):
            for x_val in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self) -> str:
        """ string representation
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """ 
        return f"[Rectangle] {self.id} {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwagrs):
        """hat assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute"""
        if args and len(args) != 0:
            for arg in args:
                
                if len(args) >= 1:
                    self.id = args[0]
                elif len(args) >= 2:
                    self.width = args[1]
                elif len(args) >= 3:
                    self.height = args[2]
                elif len(args) >= 4:
                    self.x = args[3]
                elif len(args) >= 5:
                    self.y = args[4]
        else:
            for key, value in kwagrs.items():
                setattr(self, key, value)
