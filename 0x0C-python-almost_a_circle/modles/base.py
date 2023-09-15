#!/usr/bin/python3

"""manage id attrs for all future classes"""


class Base():
    """handle id attrs"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
