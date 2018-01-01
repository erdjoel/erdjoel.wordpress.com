# Records, or structs in other languages.
# Values in a tuple can't change like lists.
# Best used as a container to hold multiple objects as one.

from collections import namedtuple

empty_tuple = tuple()  # treated as false in boolean expression.
my_birth_date_place = (1985, 'July', 2, 'Jakarta')  # non-immutable sequence of data, each position has it's own meaning

# It can be used as key in Dictionary
tuple_as_key_in_dictionary = {my_birth_date_place, 'Ridwan Julvianto'}

print(divmod(12,7))  # (1, 5): div mod return tuple of quotient (int result) and remainder of integer division
q,r = divmod(12,7)  # tuple unpacking to 2 variables
print (q)  # 1
print (r)  # 5


# A namedtuple class in the collections module allows elements to be indexed by name rather
# than position. This combines some of the advantages of a dictionary with the compactness and
# immutability of a tuple.
# e.g. An address broken into name, street, city, state and zip
employee_record = namedtuple('Employee', 'name, age, title, department, paygrade')
employee1 = employee_record("Ridwan Julvianto", 50, "tester", "test support", 9)

# Convert tuple into a list
new_list = list(employee1)

# Convert a list into a tuple

# tuples also have len(tuple), min(tuple) and max(tuple)