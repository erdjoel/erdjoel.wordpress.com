"""collections data type in Python
applies to: strings, bytes, tuples, lists, dictionaries and sets.

non-mutable

"""

# len() returns number of elements of any collection
len('aaa')

# indexing: get individual element of any collections except dictionary
# index start at zero
# use valid key value for dictionary
third_char_in_a_string = 'Pythonista'[2]

# slicing[start_index:end_index:step_size]
# not valid for dictionary and sets
# index start at 0
# start_index default is 0, end_index default is last item index, step_size default is 1
# can also goes backward: last element index is -1

'0123456789'[:]	 # start from 0 to n-1: '0123456789'
'0123456789'[3:]  # start from 3 to n-1: '3456789'
'0123456789'[:3]  # start from 0 to 3-1: '012'
'0123456789'[3:7]  # start from 3 to 7-1: '3456'
'0123456789'[3:7:2]  # from index 3 to 6, every 2 char: '35'
'0123456789'[::3]  # every 3 number from beginning to end: '0369'
'0123456789'[-3:]  # start from n-3 to n: '789'
'0123456789'[:-3]  # start from 0 to n-3: '0123456'
'0123456789'[::-3]  # every 3 number from end to beginning: '9630'

# sorted(): return sorted list
sorted('gundam')  # ['a', 'd', 'g', 'm', 'n', 'u']

# any(): True if any member of the collection is true
any(['abc', '', '3'])  # True
any(['abc', 'x', '3'])  # True

# all(): True if—and only if—all the members are true
all(['abc', '', '3'])  # False
all(['abc', 'x', '3'])  # True

# min, max
