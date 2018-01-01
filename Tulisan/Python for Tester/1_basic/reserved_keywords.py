"""with
http://effbot.org/zone/python-with-statement.htm
"""

"""print()
write to command prompt
"""

with open("tmp.txt", "w") as tmp:
    print("Hello", "World", end="END", sep="-", file=tmp)
    # use a hyphen (-) as separator
    # define the string " END" as an end marker (instead of normal EOL)
    # the content of the file should be: " Hello-WorldEND".

"""assert
https://wiki.python.org/moin/UsingAssertionsEffectively
"""

"""class
defining class
"""

"""def
defining function
"""

"""lambda
defining lambda
"""

"""del
Deletion of a name removes the binding of that name from the local or global namespace.
http://stackoverflow.com/questions/6146963/when-is-del-useful-in-python
"""
foo = "for garbage collector"
list_item = [1, 2, 3, 4, 5]
dictionary = {"alpha": 1, "beta": 2, "charlie": "c"}

del foo  # Similar effect with foo = None
del list_item[4]
del dictionary["alpha"]

"""exec"""

"""global
"""

my_var = 5


def func1():
    my_var = 42  # this only set myGlobal variable in local function scope
    print(my_var)


def func2():
    global my_var  # this override myGlobal in the module
    my_var = 30
    print(my_var)


print(my_var)  # 5
func1()  # 42
print(my_var)  # 5 -- myVar still 5
func2()  # 30
print(my_var)  # 30 -- myVar is overridden in func2

"""pass
"""

"""return
"""

"""yield
http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
"""

"""import, from, as
from urllib import request
    mine = request()  # access request directly.

import urllib.request  # used as urllib.request
mine = urllib.request()


from urllib import request as myrequest
    mine = myrequest()

http://stackoverflow.com/questions/9439480/from-import-vs-import
"""

"""and, is, or, not"""

"""if, elif, else"""

"""for, in, while, continue, break"""

"""try, except, finally, raise"""
