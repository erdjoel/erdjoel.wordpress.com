"""The None type represents a null object. There is only one None object in the Python environment,
and all references to None use that same single instance. This means that equality tests with None
are usually replaced by an identity test.

"""

a_variable = None

if a_variable is None:
    print("hooray for None")

# Don't use: a_variable == None

# None is the default return value of a Python function.
# None is considered to have a Boolean value of False .
