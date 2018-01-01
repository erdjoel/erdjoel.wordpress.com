# *args parameter receive collection of item
def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))


print_everything('apple', 'banana', 'cabbage')
print_everything(args=['apple', 'banana', 'cabbage'])


# 0. apple
# 1. banana
# 2. cabbage

# list can also be sent as the input using: *list -- will be unpacked directly
def print_three_things(a, b, c):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


my_list = ['aardvark', 'baboon', 'cat']
print_three_things(*my_list)  # the list is sent as *arg


# a = aardvark, b = baboon, c = cat

# **kwargs parameter receive Dictionary item as the input
def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


table_things(apple='fruit', cabbage='vegetable')
table_things(kwargs={'apple':'fruit', 'cabbage':'vegetable'})

# cabbage = vegetable
# apple = fruit


# dictionary can be sent as the input: **dict -- The key must match the parameter name
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action,
          "if you put", voltage, "volts through it.",
          "E's", state, "!")


d = {'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'}
parrot(**d)  # the dictionary is sent as **kwarg
# This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


