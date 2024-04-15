# Content
- Usage of Unittest method
- Usage of Doctest method

It's a common thing to name ur file test_[name of module to test].py
Also it's common to put all test files in a folder named "tests"

## Doctest

- "./learn/doctest_customer.py" file contain the class that need to be tested
The doctest method apply testing via the documentation written in the class. You run test to ur code in the interactive session and simply copy ur interactive session along with its output.

### Features
* Flags
There are many flags that ulternate the behaviour of Doctest, you still need to read more about them, you can check this website:
https://docs.python.org/3.4/library/doctest.html

* Warnings
doctest is serious about requiring exact matches in expected output. If even a single character doesn’t match, the test fails.

1) printing a dict, Python doesn’t guarantee that the key-value pairs will be printed in any particular order, so a test like:

>>> foo()
{"Hermione": "hippogryph", "Harry": "broomstick"}

is vulnerable!

Instead:

>>> d = sorted(foo().items())
>>> d
[('Harry', 'broomstick'), ('Hermione', 'hippogryph')]

2) Another bad idea is to print things that embed an object address,

3) Floating-point numbers are also subject to small output variations across platforms,

>>> 1./7  # risky
0.14285714285714285
>>> print(1./7) # safer
0.142857142857
>>> print(round(1./7, 6)) # much safer
0.142857


### Steps:
1) Run ur tests in interactive mode
2) Copy ur interactive session and paste it inside ur doc of class or func
3) Add this code at the bottom of ur module
if __name__ == "__main__":
    import doctest
    doctest.testmod()

4) Run ur module using this code
python3 module_name.py -v

## Unittest

- "customer.py" file contain the class "Customer" that we will test with unit testing
- "test_customer.py" is the file containg the unit testing code, it's a common python convention to name test file like this:
"test_[name of module to be tested].py"_

### Notes:
1) If you encountered a bug and you found the cause of it, It's best practice to add a test case to it so you don't fall in the same hole again

2) Check file "calc.py" and "test-calc.py" in learn to know more

### Steps:
1) first => import unittest
2) second => from customer import Customer
3) your test class should have a good name and copy "unittest.TestCase" class

class TestCustomer(unittest.TestCase):


4) if ur code is object based u can use setUp method

def setUp(self):
        self.customer_1 = Customer('John', 'Brad', 5000)
        self.customer_2 = Customer('Tina', 'Smith', 3000)

To avoid recreating ur objects insied each and every method

5) Use different assertion inside test method
Note that test method should follow this naming convention:
test_[customer_mail]

def test_customer_fullname(self):
        self.assertEqual(self.customer_1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer_2.customer_fullname, 'Tina Smith')

6) End test file with:

if __name__ === '__main__':
	unittest.main()

7) To run our test from command line without doing step "6" you can run the code:
python3 -m unittest test-calc.py
