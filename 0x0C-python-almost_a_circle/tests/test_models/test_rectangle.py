#!/usr/bin/python3
""" Test for Base class """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Test Base Class """

    def test_id(self):
        """ test id case """
        Rectangle.reset()
        b1 = Rectangle(10, 20)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 20)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)


if __name__ == '__main__':
    unittest.main()
