#!/use/bin/python3

"""only square class"""

from modles.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, val):
        """size setter"""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be greater than zero!")
        self.width = val
        self.height = val

    def __str__(self):
        """string representation"""
        return f"[Square]\
            ({self.id})  {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
