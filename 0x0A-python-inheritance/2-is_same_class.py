#!/usr/bin/python3
""" is instance module """


def is_same_class(obj, a_class):
    """ is same class function
    Args:
        obj: object ot be checked
        a_class: class to be checked with

    Returns:
        True if it's from same class
    """
    return isinstance(obj, a_class)
