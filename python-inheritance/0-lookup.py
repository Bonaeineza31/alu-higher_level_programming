#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attrib and methods of an obj. 
    Args:
        obj:obj whose attributes and methods are to be retrieved.
    Returns:
        A list of the object's attributes and methods.
    """
    return dir(obj)
