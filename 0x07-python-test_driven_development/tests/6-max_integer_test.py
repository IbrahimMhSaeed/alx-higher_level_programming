#!/usr/bin/python3
""" This is my unittest module """


import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This is my unittest class """

    def test_len(self):
        """ test if len of list is 0 """
        self.assertEqual(max_int(), None)
        self.assertEqual(max_int([]), None)


    def test_max(self):
        """ test for max value """
        self.assertEqual(max_int([1, 2, 3]), 3)
        self.assertEqual(max_int([-1, -2, -3]), -1)
        self.assertEqual(max_int([123333, 2334, 999]), 123333)
        self.assertEqual(max_int([2]), 2))
        self.assertEqual(max_int([1, 3, 2]), 3)
