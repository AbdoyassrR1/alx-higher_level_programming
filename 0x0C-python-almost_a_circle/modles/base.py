#!/usr/bin/python3

"""manage id attrs for all future classes"""

import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        target = cls.__name__ + ".json"
        list_of_dicts = []
        with open(target, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    dic = obj.to_dictionary()
                    list_of_dicts.append(dic)
                file.write(cls.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                inst = cls(4, 16)
            if cls.__name__ == "Square":
                inst = cls(4)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """
        Args: a class cls
        returns a list of instances
        """
        instance_list = []
        file = cls.__name__ + ".json"
        if not os.path.exists(file):
            return []
        with open(file, "r") as f:
            json_str = f.read()
            loaded_list = cls.from_json_string(json_str)
            for dict in loaded_list:
                inst = cls.create(**dict)
                instance_list.append(inst)

        return instance_list
