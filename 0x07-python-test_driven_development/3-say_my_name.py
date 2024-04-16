#!/usr/bin/python3
""" This is say my name module """


def say_my_name(first_name, last_name=""):
    """ Say my name <first_name> + <second_name>

    Args:
        first_name (str): the first name
        last_name (str): the second name

    Returns:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name == "":
        first_name = "Bob"

    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc = abc + abc.upper()
    abc = set(abc)

    print("My name is ", end="")
    
    for c in first_name:
        if c in abc:
            print(c, end="")
    print(" ", end="")

    for c in last_name:
        if c in abc:
            print(c, end="")
    print("")
