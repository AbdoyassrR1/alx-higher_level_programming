#!/usr/bin/python3
"""This module is about a class Student that defines a student
"""


class Student:
    """Public instance attributes: first_name
       last_name and age
    """

    def __init__(self, first_name, last_name, age):
        """_summary_
        Args:
        first_name (_type_)
        last_name (_type_)
        age (_type_)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:

            return self.__dict__
        if all(type(attr) is str for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        """

        for key, value in json.items():
            setattr(self, key, value)
