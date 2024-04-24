# Almost a circle 

**Content:**

- args and kwargs
- Serialization/Deserialization
- JSON

## `*args` and `**Kwargs`

First of all let me tell you that it is not necessary to write `*args` or `**kwargs`. Only the `*` (aesteric) is necessary. You could have also written `*var` and `**vars`. Writing `*args` and `**kwargs` is just a convention.

### Usage of `*args`
`*args` and `**kwargs` are mostly used in function definitions. `*args` and `**kwargs` allow you to pass a variable number of arguments to a function.

```
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')

# OUPUT

first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test
```

### Usage of `**kwargs`

if you want to handle named arguments in a function. 

```
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print("%s == %s" %(key,value))
 
>>> greet_me(name="yasoob")
name == yasoob
```

### Using `*args` and `**kwargs` to call a function

```
def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3
```
Now you can use `*args` or `**kwargs` to pass arguments to this little function.

```
# first with *args
>>> args = ("two", 3,5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two","arg1":5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

## unittest — Unit testing framework

It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections.

### Basics Usage Example

```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

### Command-Line Interface

```
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```

You can run tests with more detail (higher verbosity) by passing in the -v flag:

```
python -m unittest -v test_module
```

For a list of all the command-line options:

```
python -m unittest -h
```

### Test Discovery

Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be modules or packages importable from the top-level directory of the project *(this means that their filenames must be valid identifiers)*.

#### Implementing Test Discovery

Test discovery is implemented in `TestLoader.discover()`, but can also be used from the command line.

The basic command-line usage is:

```
cd project_directory
python -m unittest discover
```

*Note: As a shortcut, `python -m unittest` is the equivalent of `python -m unittest discover`*

**The `discover` sub-command has the following options:**

|option	|meaning
|-------|--------------
| -v --verbose	|Verbose output
| -s, --start-directory directory	|Directory to start discovery (. default)
| -p, --pattern pattern	|Pattern to match test files (`test*.py` default)
| -t, --top-level-directory directory	|Top level directory of project (defaults to start directory)

**Example usage of Flags**

```
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"
```
### Organizing test code

The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for correctness. In unittest, test cases are represented by unittest.TestCase instances. To make your own test cases you must write subclasses of TestCase or use FunctionTestCase.

The testing code of a TestCase instance should be entirely self contained, such that it can be run either in isolation or in arbitrary combination with any number of other test cases.

Tests can be numerous, and their set-up can be repetitive. Luckily, we have a method called `setUp()`, which the testing framework will automatically call for every single test we run:
```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```

Similarly, we can provide a `tearDown()` method that tidies up after the test method has been run:
```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```
If `setUp()` succeeded, `tearDown()` will be run whether the test method succeeded or not.

*It is recommended that you use TestCase implementations to group tests together according to the features they test.*

**You can use `TestSuit` Class**
```
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

#### Where to Place Your Test Code

You can place the definitions of test cases and test suites in the same modules as the code they are to test (such as `widget.py`), but there are several advantages to placing the test code in a separate module, such as `test_widget.py`:

- The test module can be run standalone from the command line.
- The test code can more easily be separated from shipped code.
- There is less temptation to change test code to fit the code it tests without a good reason.
- Test code should be modified much less frequently than the code it tests.
- Tested code can be refactored more easily.
- Tests for modules written in C must be in separate modules anyway, so why not be consistent?
- If the testing strategy changes, there is no need to change the source code.

### Skipping tests and expected failures

- Unittest supports skipping individual test methods and even whole classes of tests.
- In addition, it supports marking a test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a TestResult.

```
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
```

This is the output of running the example above in verbose mode:
```
test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK (skipped=4)
```
Classes can be skipped just like methods:
```
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```
Expected failures use the expectedFailure() decorator.
```
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```

#### Decorators for Skipping and Expected Failures:


- `@unittest.skip(reason)`

	Unconditionally skip the decorated test. reason should describe why the test is being skipped.

- `@unittest.skipIf(condition, reason)`

    Skip the decorated test if condition is true.

- `@unittest.skipUnless(condition, reason)`

    Skip the decorated test unless condition is true.

- `@unittest.expectedFailure`

    Mark the test as an expected failure or error. If the test fails or errors in the test function itself (rather than in one of the test fixture methods) then it will be considered a success. If the test passes, it will be considered a failure.

- `exception unittest.SkipTest(reason)`

    This exception is raised to skip a test.

### Extra Reading

|Method				|Checks that
|-------------------------------|------------------------
|assertEqual(a, b)		|a == b
|assertNotEqual(a, b)		|a != b
|assertTrue(x)			|bool(x) is True
|assertFalse(x)			|bool(x) is False
|assertIs(a, b)			|a is b
|assertIsNot(a, b)		|a is not b
|assertIsNone(x)		|x is None
|assertIsNotNone(x)		|x is not None
|assertIn(a, b)			|a in b
|assertNotIn(a, b)		|a not in b
|assertIsInstance(a, b)		|isinstance(a, b)
|assertNotIsInstance(a, b)	|not isinstance(a, b)
