"""
Python variables are just names.

Variables do not have a type; it is the object to which they are bound that has a type.
The name is just a label and, as such, it can be reassigned to a completely different object.

"""

an_int = 6
int_alias = an_int

print(an_int == int_alias)  # True: same value
print(an_int is int_alias)  # True: refer to same object

a_string = "I love spam"
another_string = "I love spam"

print(a_string == another_string)  # True: equal value
print(a_string is another_string)  # False: refer to different object
