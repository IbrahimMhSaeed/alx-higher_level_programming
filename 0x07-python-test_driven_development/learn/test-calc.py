import unittest
import calc

class TestCalc(unittest.TestCase):
    """ Test cases for calc module """

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    # Same is done for all other Method

    # How to check for Exception Errors

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(1, -1), -1)
        self.assertEqual(calc.div(-1, -1), 1)

        # This is the Exception Error Example
        with self.assertRaises(ValueError):
            calc.div(1, 0)
