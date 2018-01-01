"""
Comparisons to None should always be done with is or is not
if foo is not None:  # Yes. it is more readable.
if not foo is None:  # No. valid but not as readable as above

Object type comparisons should always use isinstance() instead of comparing types directly.
if isinstance(obj, int):  # Yes
if type(obj) is type(1):  # No

Don't compare boolean values to True or False using == .
if greeting:  # Yes
if greeting == True:  # No
if greeting is True:  # Noooo

Python shortcut to handle boundary comparison
if lowerLimit < avalue < upperLimit:  # equals to (aValue < upperLimit) and (aValue > lowerLimit):

Comparison Operators : ==, !=, >, <, >=, <=
"""

# combine conditions with logical operators: and, or, not
age = 15
if (age >= 1) and (age <= 18):
    print("You get a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not (age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party yeah")

# Another form: conditional expression selector.
# <a value> if <an expression> else <another value>
weather = 'sunny'
breakfast = ''

breakfast = 'cake' if weather == 'rain' else 'donut'  # another sample

# expanded form
if weathet == 'rain':
    breakfast = 'cake'
else:
    breakfast = 'donut'
