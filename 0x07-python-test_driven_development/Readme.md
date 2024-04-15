# Content
- Usage of Unittest method
- Usage of Doctest method

It's a common thing to name ur file test_[name of module to test].py
Also it's common to put all test files in a folder named "tests"

## Doctest

- "./learn/doctest_customer.py" file contain the class that need to be tested
The doctest method apply testing via the documentation written in the class. You run test to ur code in the interactive session and simply copy ur interactive session along with its output.

**It's always recommended to put all ur test in "test" folder**
**You should put ur test in `test_customer.txt` file and import ur tested module inside**

### Features

#### Option Flags
There are many flags that ulternate the behaviour of Doctest, you still need to read more about them, you can check this website:


`DONT_ACCEPT_TRUE_FOR_1`
True != 1

`DONT_ACCEPT_BLANKLINE`
canceling this option <BLANKLINE>

`NORMALIZE_WHITESPACE`
all sequences of whitespace (blanks and newlines) are treated as equal

`ELLIPSIS`
When specified, an ellipsis marker (...) in the expected output can match any substring in the actual output.

`IGNORE_EXCEPTION_DETAIL`
an exception passes if an exception of the expected type is raised

`SKIP`
Simply ignore test


#### Warnings
doctest is serious about requiring exact matches in expected output. If even a single character doesn’t match, the test fails.

1) printing a dict, Python doesn’t guarantee that the key-value pairs will be printed in any particular order, so a test like:
```
>>> foo()
{"Hermione": "hippogryph", "Harry": "broomstick"}
```
is vulnerable!

Instead:
```
>>> d = sorted(foo().items())
>>> d
[('Harry', 'broomstick'), ('Hermione', 'hippogryph')]
```
2) Another bad idea is to print things that embed an object address,

3) Floating-point numbers are also subject to small output variations across platforms,
```
>>> 1./7  # risky
0.14285714285714285
>>> print(1./7) # safer
0.142857142857
>>> print(round(1./7, 6)) # much safer
0.142857
```

### Steps:
1) Run ur tests in interactive mode

2) Copy ur interactive session and paste it inside ur doc of class or func
- you can alternativly put them in `.txt` file as recommended

3) Add this code at the bottom of ur module
```
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
if you add it you will not need to import the module in ur test session

4) Run ur module using
- Direct run of module
```
python3 module_name.py -v
```
- Run doctest module with command line args
```
python -m doctest -v example.py[or .txt]
```

### Usage of doctest with flags

```
"""
>>> print(list(range(20))) # doctest: +NORMALIZE_WHITESPACE
[0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
10,  11, 12, 13, 14, 15, 16, 17, 18, 19]

>>> print(list(range(20))) # doctest: +ELLIPSIS
[0, 1, ..., 18, 19]

>>> print(list(range(20))) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]
"""
```

## Unittest

- `customer.py` file contain the class `Customer` that we will test with unit testing
- `test_customer.py` is the file containg the unit testing code, it's a common python convention to name test file like this:
`test_[name of module to be tested].py`

### Notes:
1) If you encountered a bug and you found the cause of it, It's best practice to add a test case to it so you don't fall in the same hole again

2) Check file "calc.py" and "test-calc.py" in learn for more examples

### Steps:
1) first => import unittest
2) second => from customer import Customer
3) your test class should have a good name and copy "unittest.TestCase" class
```
class TestCustomer(unittest.TestCase):
```

4) if ur code is object based u can use setUp method
```
def setUp(self):
        self.customer_1 = Customer('John', 'Brad', 5000)
        self.customer_2 = Customer('Tina', 'Smith', 3000)
```
To avoid recreating ur objects insied each and every method

5) Use different assertion inside test method
Note that test method should follow this naming convention:
test_[customer_mail]
```
def test_customer_fullname(self):
        self.assertEqual(self.customer_1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer_2.customer_fullname, 'Tina Smith')
```
6) End test file with:

```
if __name__ === '__main__':
	unittest.main()
```
7) To run our test from command line without doing step "6" you can run the code:
```
python3 -m unittest test-calc.py
```

## Optional Reading

###

### Different Assertion Methods

|Method 	|Checks that|
|---------------|-----------
|assertEqual(a, b) 	|a == b|
|assertNotEqual(a, b) 	|a != b|
|assertTrue(x) 	bool(x) |is True|
|assertFalse(x) 	|bool(x) is False|
|assertIs(a, b) 	|a is b|
|assertIsNot(a, b) 	|a is not b|
|assertIsNone(x) 	|x is None|
|assertIsNotNone(x) 	|x is not None|
|assertIn(a, b) 	|a in b|
|assertNotIn(a, b) 	|a not in b|
|assertIsInstance(a, b) 	|isinstance(a, b)|
|assertNotIsInstance(a, b) 	|not isinstance(a, b)|
