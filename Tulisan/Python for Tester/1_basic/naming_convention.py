#!/usr/bin/env python  # shebang line to denote unix-based system to use whichever default python in your current environment #noqa
# -*- coding: utf-8 -*-
# see PEP 263 -- Defining Python Source Code Encodings
# used by the Python parser to interpret the file using the given encoding

"""This module's docstring summary line.
This is a multi-line docstring. Paragraphs are separated with blank lines.
Lines conform to 79-char limit. Use double-quote

Write docstrings for ALL modules, public classes, funcs and methods.""

this documentation displayed as part of the built-in help() output for that object.
e.g. help(ClassName) or help(function_name)

a 79-char ruler:
# 34567891123456789212345678931234567894123456789512345678961234567897123456789

convention:
module_name, package_name,
ClassName, ExceptionName,
function_name, method_name,
CONSTANT_NAME, var_name, parameter_name

"""


# 2 empty lines between top-level classes
class NamingConvention(object):
    """Write docstrings for ALL public classes, funcs and methods.
    First line of a docstring is short and next to the quotes.
    Closing quotes are on their own line
    """

    A_CONSTANT = "ugh."

    a = 2  # Public attributes have no leading underscores.
    # if your public attribute collides with reserved keyword,
    # use single trailing underscore to avoid conflict
    class_ = 'foo'

    _internal_variable = 3  # _single_leading_underscore for "internal use" indicator.

    # this __double_leading_underscore will trigger name mangling
    # e.g. inside class FooBar, __boo becomes _FooBar__boo
    # for attributes that you do not want subclasses to use (your subclass may have the same name)
    # private internal variable
    __internal_var = 4

    # NEVER use double leading and trailing underscores for your own names
    # "magic" objects or attributes that live in controlled namespaces.
    # E.g.__init__, __import__ or __file__.
    # Never invent such names, only use them as documented.
    __nooooooodontdoit__ = 0

    # don't use small l, big-O, big-I letter as single letter variable name
    # because some fonts are hard to distiguish
    l = 1
    O = 2
    I = 3

    # You use self when:
    # 1. Defining an instance method.
    #       The instance is passed automatically as the first parameter when you call a method on an instance.
    # 2. Referencing a class or instance attribute from inside an instance method.
    #       If you want to call a method or access a name (variable) on the instance the method was called on.

    # some examples of how to wrap code to conform to 79-columns limit:
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if width == 0 and height == 0 and \
           color == 'red' and emphasis == 'strong' or \
           highlight > 100:
            raise ValueError('sorry, you lose')
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        NamingConvention.__init__(self, width, height,
                      color, emphasis, highlight)

    def long_function_name(self, var_one, var_two,
                           var_three, var_four):
        a = 5
        b = 9  # Using # noqa in the end of this line makes flake8 give no warnings about line length! # noqa
        c = (a + b) * (a - b)  # operator spacing should improve readability.
        return a, b, c

    # empty lines within method to enhance readability; no set rule
    short_foo_dict = {'loooooooooooooooooooong_element_name': 'cat',
                      'other_element': 'dog'}

    foo = long_function_name('var_one', 'var_two',
                             'var_three', 'var_four')

    # align the variable name
    this_is_one_thing = True
    that_is_another_thing = False
    if (this_is_one_thing
            and that_is_another_thing):
        foo()

    # Backslashes may still be appropriate at times. For example, long,
    # multiple with -statements cannot use implicit continuation, so backslashes are acceptable:
    with open('/path/to/some/file/you/want/to/read') as file_1, \
            open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())

    long_foo_dict_with_many_elements = {
        'foo': 'cat',
        'bar': 'dog'
    }

    # Yes: easy to match operators with operands
    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest)

    # 1 empty line between in-class def'ns
    def foo_method(self, x, y=None):
        """Method and function names are lower_case_with_underscores.
        Always use self as first argument to instance methods.
        """
        pass


# 2 empty lines between top-level functions
def top_level_functions(self):
    """do something here"""


if __name__ == "__main__":
    """Running this module
    If this module ran by Python Interpreter, __name__ will be set as "__main__"
    If this module called by other module, __name__ will be set as module_name
    
    best practice: if this file is intended as module, you can put Unit Test Code here
    so you can always call this file directly to test it
    """
    NamingConvention()

# Newline at end of file
