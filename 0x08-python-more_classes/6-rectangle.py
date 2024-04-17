#!/usr/bin/python3
""" This is my Rectangle Module """


class Rectangle:
    """ This is my Rectangle class """
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ init function to initialize """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter function """
        return self.__width

    @property
    def height(self):
        """ getter fucntion """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter fucntion """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ setter function """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calc and return area """
        return self.__width * self.__height

    def perimeter(self):
        """ calc and return perimeter """
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ str to be printed """
        if self.__width == 0 or self.height == 0:
            return ""
        else:
            p = ("#" * self.__width + "\n") * (self.__height - 1)
            p = p + ("#" * self.__width)
            return p

    def __repr__(self):
        """ repr for class """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ deletion message """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
