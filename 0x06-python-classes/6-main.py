#!/usr/bin/python3
Square = __import__('6-square').Square

try:
    my_square = Square(3, (1, -3))
    my_square.my_print()
except Exception as ex:
    print(ex)

print("--")
