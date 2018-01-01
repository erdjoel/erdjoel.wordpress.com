## Beginning Test-Driven Development in Python ##

*using the nosetests unit-testing package*

### What Is Test-Driven Development? ###

TDD, in its most basic terms, is the process of implementing code by writing your tests first, seeing them fail, then writing the code to make the tests pass. You can then build upon this developed code by appropriately altering your test to expect the outcome of additional functionality, then writing the code to make it pass again.

TDD brings out a natural tendency to think about your problem first. While you start to construct your test, you have to think about the way you design your code. What will this method return? What if we get an exception here? And so on. 

By developing in this way, it means you consider the different routes through the code, and cover these with tests as needed. This approach allows you to escape the trap that many developers fall into (myself included): diving into a problem and writing code exclusively for the first solution you need to handle.


The process can be defined as such:

1. Write a failing unit test
2. Make the unit test pass
3. Refactor
4. Repeat this process for every feature, as is necessary.

### Syntax for Unit Testing ###

The main methods that we make use of in unit testing for Python are:

- ***assert***: base assert allowing you to write your own assertions
- ***assertEqual(a, b)***: check a and b are equal
- ***assertNotEqual(a, b)***: check a and b are not equal
- ***assertIn(a, b)***: check that a is in the item b
- ***assertNotIn(a, b)***: check that a is not in the item b
- ***assertFalse(a)***: check that the value of a is False
- ***assertTrue(a)***: check the value of a is True
- ***assertIsInstance(a, TYPE)***: check that a is of type "TYPE"
- ***assertRaises(ERROR, a, args)***: check that when a is called with args that it raises ERROR

For more methods available, see the *Python Unit Test Docs*.

### Installing and Using Python's Nose ###

note: use virtualenv to keeps all the packages for various projects separate.

to install: 

`pip install nose`

to execute a single test file:

`$ nosetests example_unit_test.py`

Or execute a suite of tests in a folder.

`$ nosetests /path/to/tests`

Standard to follow: begin each test's method with `test_` to ensure that the nosetest runner can find your tests!

**Options**

Some useful command line options:

- `-v`: gives more verbose output, including the names of the tests being executed.
- `-s` or `-nocapture`: allows output of print statements, which are normally captured and hidden while executing tests. Useful for debugging.
- `--nologcapture`: allows output of logging information.
- `--rednose`: an optional plugin, which can be downloaded, but provides colored output for the tests.
- `--tags=TAGS`: allows you to place an @TAG above a specific test to only execute those, rather than the entire test suite.

### Example Problem and Test-Driven Approach ###

We will write a very simple calculator class, with add, subtract and other simple methods as you would expect. 

Following a TDD approach, let's say that we have a requirement for an add function, which will determine the sum of two numbers, and return the output. Let's write a failing test for this. 

In an empty project, create two python packages app and test. To make them Python packages (and thus support importing of the files in the tests later on), create an empty file called __init__.py, in each directory. This is Python's standard structure for projects and must be done to allow item to be importable across the directory structure. For a better understanding of this structure, you can refer to the Python packages documentation. Create a file named test_calculator.py in the test directory with the following contents.

```python
import unittest
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
```

Writing the test is fairly simple.

First, we import the standard unittest module from the Python standard library.

Next, we need a class to contain the different test cases.

Finally, a method is required for the test itself, with the only requirement being that it is named with "test_" at the beginning, so that it may be picked up and executed by the nosetest runner, which we will cover shortly.

With the structure in place, we can then write the test code. We initialize our calculator so that we can execute the methods on it. Following this, we can then call the add method which we wish to test, and store its value in the variable, result. Once this is complete, we can then make use of unittest's assertEqual method to ensure that our calculator's add method behaves as expected.

Now you will use the nosetest runner to execute the test. You could execute the test using the standard unittest runner, if you wish, by adding the following block of code to the end of your test file.

```python
if __name__ == '__main__':
    unittest.main()
```

This will allow you to run the test using the standard way of executing Python files, $ python test_calculator.py. However, for this tutorial you are going to make use of the nosetests runner, which has some nice features such as being able to execute nose tests against a directory and running all tests, amongst other useful features.

`$ nosetests test_calculator.py`

```
======================================================================
ERROR: test_calculator_add_method_returns_correct_result (test.test_calculator.TddInPythonExample)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/tdd_in_python/test/test_calculator.py", line 6, in test_calculator_add_method_returns_correct_result
    calc = Calculator()
NameError: global name 'Calculator' is not defined
 
----------------------------------------------------------------------
Ran 1 test in 0.001s
 
FAILED (errors=1)
```

From the output nosetest has given us, we can see that the problem relates to us not importing Calculator. That's because we haven't created it yet! So let's go and define our Calculator in a file named calculator.py under the app directory and import it:

```python
class Calculator(object):
 
    def add(self, x, y):
        pass
```
```python
import unittest
from app.calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
 
 
if __name__ == '__main__':
    unittest.main()
```

Now that we have Calculator defined, let's see what nosetest indicates to us now:

`$ nosetests test_calculator.py`
```
======================================================================
FAIL: test_calculator_add_method_returns_correct_result (test.test_calculator.TddInPythonExample)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/tdd_in_python/test/test_calculator.py", line 9, in test_calculator_add_method_returns_correct_result
    self.assertEqual(4, result)
AssertionError: 4 != None
 
----------------------------------------------------------------------
Ran 1 test in 0.001s
 
FAILED (failures=1)
```

So, obviously, our add method is returning the wrong value, as it doesn't do anything at the moment. Handily, nosetest gives us the offending line in the test, and we can then confirm what we need to change. Let's fix the method and see if our test passes now:

```python
class Calculator(object):
 
    def add(self, x, y):
        return x+y
```

`$ nosetests test_calculator.py`
```
----------------------------------------------------------------------
Ran 1 test in 0.000s
 
OK
```

Success! We have defined our add method and it works as expected. However, there is more work to do around this method to ensure that we have tested it properly.

We have fallen into the trap of just testing the case we are interested in at the moment.

What would happen if someone were to add anything other than numbers? Python will actually allow for the addition of strings and other types, but in our case, for our calculator, it makes sense to only allow adding of numbers. Let's add another failing test for this case, making use of the assertRaises method to test if an exception is raised here:

```python
import unittest
from app.calculator import Calculator

 
class TddInPythonExample(unittest.TestCase):
 
    def setUp(self):
        self.calc = Calculator()
 
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
 
 
if __name__ == '__main__':
    unittest.main()
```

You can see from above that we added the test and are now checking for a ValueError to be raised, if we pass in strings. We could also add more checks for other types, but for now, we'll keep things simple. 

You may also notice that we've made use of the setup() method. This allows us to put things in place before each test case. So, as we need our Calculator object to be available in both test cases, it makes sense to initialize this in the setUp method. 

Let's see what nosetest indicates to us now:

`$ nosetests test_calculator.py`
```
======================================================================
FAIL: test_calculator_returns_error_message_if_both_args_not_numbers (test.test_calculator.TddInPythonExample)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/tdd_in_python/test/test_calculator.py", line 15, in test_calculator_returns_error_message_if_both_args_not_numbers
    self.assertRaises(ValueError, self.calc.add, 'two', 'three')
AssertionError: ValueError not raised
 
----------------------------------------------------------------------
Ran 2 tests in 0.001s
 
FAILED (failures=1)
```

Clearly, nosetests indicates to us that we are not raising the ValueError when we expect to be. Now that we have a new failing test, we can code the solution to make it pass.
```
class Calculator(object):
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
```

From the code above, you can see that we've added a small addition to check the types of the values and whether they match what we want. One approach to this problem could mean that you follow duck typing, and simply attempt to use it as a number, and "try/except" the errors that would be raised in other cases. The above is a bit of an edge case and means we must check before moving forward. As mentioned earlier, strings can be concatenated with the plus symbol, so we only want to allow numbers. Utilising the isinstance method allows us to ensure that the provided values can only be numbers.

To complete the testing, there are a couple of different cases that we can add. As there are two variables, it means that both could potentially not be numbers. Add the test case to cover all the scenarios.

```
import unittest
from app.calculator import Calculator
 
 
class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
 
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
 
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
 
 
if __name__ == '__main__':
    unittest.main()

```

When we run all these tests now, we can confirm that the method meets our requirements!

`$ nosetests test_calculator.py`
```
----------------------------------------------------------------------
Ran 4 tests in 0.001s
 
OK
```

###Debug Code With PDB###

One of the most commonly used tools is pdb (or Python Debugger). The tool is included in the standard library and simply requires adding one line where you would like to stop the program execution and enter into pdb, typically known as the "breakpoint". Using our failing code in the add method, try adding the following line before the two values are subtracted.

```python
class Calculator(object):
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb; pdb.set_trace()
            return x - y
        else:
            raise ValueError
```

If using nosetest to execute the test, be sure to execute using the -s flag which tells nosetest to not capture standard output, otherwise your test will just hang and not give you the pdb prompt. Using the standard unittest runner and pytest does not require such a step.

With the pdb code snippet in place, when you execute the test now, the execution of the code will break at the point at which you placed the pdb line, and allow you to interact with the code and variables that are currently loaded at the point of execution. When the execution first stops and you are given the pdb prompt, try typing list to see where you are in the code and what line you are currently at.

```$ nosetests -s
> /Users/user/PycharmProjects/tdd_in_python/app/calculator.py(7)add()
-> return x - y
(Pdb) list
  2          def add(self, x, y):
  3             number_types = (int, long, float, complex)
  4    
  5             if isinstance(x, number_types) and isinstance(y, number_types):
  6                 import pdb; pdb.set_trace()
  7  ->              return x - y
  8             else:
  9                 raise ValueError
[EOF]
(Pdb)
```

You can interact with your code, as if you were within a Python prompt, so try evaluating what is in the x and y variables at this point.

```
(Pdb) x

(Pdb) y
```

You can continue to "play" around with the code as you require to figure out what is wrong. You can type help at any point to get a list of commands, but the core set you will likely need are:

- ***n***: step forward to next line of execution.
- ***list***: show five lines either side of where you are currently executing to see the code involved with the current execution point.
- ***args***: list the variables involved in the current execution point.
- ***continue***: run the code through to completion.
- ***jump <line number>***: run the code until the specified line number.
- ***quit/exit***: stop pdb.