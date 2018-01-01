"""Standard format
try:
    A block of application code
except <an error type> as <anExceptionObject>:
    A block of error handling code
    # exception object contains details of where the exception occurred
    # and provides a string conversion method so that a meaningful error message may be printed
except <another error type>:
    # omit the as … part if the exception details are not required
    A block of other error handling code
except ('TuplesOf', 'ErrorType'):
    A block of error handling code for all error in the tuple
else:
    Another block of application code  # executed if the try block succeeds without any errors
finally:
    A block of clean-up code

At least one of except or finally must exist
There can be multiple except clauses, but only one else or finally.

"""

try:
    raise ValueError('wrong value')
except ValueError as error:
    print(error.args)  # 'wrong value',

# default exceptions:
"""
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StandardError
| +-- BufferError
| +-- ArithmeticError
| | +-- FloatingPointError
| | +-- OverflowError
| | +-- ZeroDivisionError
| +-- AssertionError
| +-- AttributeError
| +-- EnvironmentError
| | +-- IOError
| | +-- OSError
| | +-- WindowsError(Windows)
| | +-- VMSError(VMS)
| +-- EOFError
| +-- ImportError
| +-- LookupError
| | +-- IndexError
| | +-- KeyError
| +-- MemoryError
| +-- NameError
| | +-- UnboundLocalError
| +-- ReferenceError
| +-- RuntimeError
| | +-- NotImplementedError
| +-- SyntaxError
| | +-- IndentationError
| | +-- TabError
| +-- SystemError
| +-- TypeError
| +-- ValueError
| +-- UnicodeError
| +-- UnicodeDecodeError
| +-- UnicodeEncodeError
| +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
"""


# exceptClass.py
class TestNumber(object):
    def __init__(self, number):
        self.number = number

    def return_values(self):
        try:
            if type(self.number) is int:
                return "The values are: ", self.number, type(self.number)  # Returns a tuple with 3 item (implicitly)
            else:
                raise NotNumberError(self.number)
        except NotNumberError as e:
            print("The value for number must be an int you passed: ", e.value)


class NotNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
