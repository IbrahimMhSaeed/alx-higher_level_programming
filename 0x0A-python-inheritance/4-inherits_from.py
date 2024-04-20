#!/usr/bin/python3
""" Sub class module """


def inherits_from(obj, a_class):
    """ inherits form function """
    if obj.__class__ == a_class:
        return False
    return issubclass(obj.__class__, a_class)
