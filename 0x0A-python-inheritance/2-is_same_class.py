#!/usr/bin/python3

"""this module is containing a def is_same_class(obj, a_class) function"""


def is_same_class(obj, a_class):
    
    """function that returns True if the object is 
    exactly an instance of the specified class ; otherwise False."""
    
    
    issame = True

    if isinstance(obj, a_class) == True:
        return issame
    else:
        issame = False
        return issame
