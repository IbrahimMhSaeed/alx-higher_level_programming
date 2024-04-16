#!/usr/bin/python3
""" This is my Square module """


def print_square(size):
    """ This is my square fuction """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
