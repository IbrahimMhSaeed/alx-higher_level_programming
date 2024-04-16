#!/usr/bin/python3
""" Module contain function that adds two numbers """


def add_integer(a, b=98):
    """ fuction adds two numbers.

    Args:
        a (int, float): first number
        b (int, float): second number

    Returns:
        int: Summation of the two numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)

    return a + b
