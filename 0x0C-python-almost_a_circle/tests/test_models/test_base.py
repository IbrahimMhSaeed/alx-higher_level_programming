#!/usr/bin/python3
""" Test for Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Test Base Class """

    def test_id(self):
        """ test id case """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(1)
        self.assertEqual(b3.id, 1)
        b4 = Base(1)
        self.assertEqual(b4.id, 1)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        b6 = Base(-22)
        self.assertEqual(b6.id, -22)
        b7 = Base(0)
        self.assertEqual(b7.id, 0)

if __name__ == '__main__':
    print(Base)
    unittest.main()
