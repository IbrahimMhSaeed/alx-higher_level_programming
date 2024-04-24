#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Generic Getter """
        return self.__width

    @property
    def height(self):
        """ Generic Getter """
        return self.__height

    @property
    def x(self):
        """ Generic Getter """
        return self.__x

    @property
    def y(self):
        """ Generic Getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ Generic Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Generic Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Generic Setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Generic Setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ compute area method """
        return self.width * self.height

    def display(self):
        """ display rectangle """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ string printed for class """
        return_str = f"[Rectangle] ({self.id}) "
        return_str += f"{self.x}/{self.y} - {self.width}/{self.height}"
        return return_str

    def update(self, *args, **kwargs):
        """ update values """
        if args:
            if len(args) != 0:
                ll = ["id", "width", "height", "x", "y"]
                for name, i in zip(ll, range(len(args))):
                    setattr(self, name, args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Rectangle dictionary """
        return self.__dict__
