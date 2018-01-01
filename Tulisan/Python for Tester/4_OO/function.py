"""define functions

def functionName(parameter1, param2,...):
    function block


returns None by default

"""

import math


# Be consistent in return statements in a function
# Yes
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None


# Yes
def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


# No
def foo(x):
    if x >= 0:
        return math.sqrt(x)


# No
def bar(x):
    if x < 0:
        return
    return math.sqrt(x)


# lambda function: PEP 8: do not use lambda. Use def statement.
f = lambda x: 2 * x


def f(x): return 2 * x  # def statement provide clearer intention than it's lambda counterpart


straight_line = lambda m, x, c: m * x + c  # def straight_line(m,x,c): return m*x+c

straight_line(2, 4, -3)

# variables that are declared outside a function and only referenced inside a function are implicitly global.
# If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local
# unless explicitly declared as global.

