#!/usr/bin/python3
""" rectangle class  module """

class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ raise error """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if not (value.__class__ ==  int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ BaseGeometry class """
    def __init__(self, width, height):
        """ initialize values """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string description of class """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
