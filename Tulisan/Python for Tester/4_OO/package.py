"""Creating package
A package is essentially a folder of modules that contain a file called __init__ .py

Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

__init__ .py is a python file that may be empty and will be loaded when you import the package.
Usually define __all__ list to control visibility

another best practice: have common.py at the top level of the package and having all of the other modules import
common. This enable included modules to have a set of functions or data shared between them.

"""

import os.path  # importing module path in os package. and also all os module.
# Python automatically executes all of the __init__.py files that it finds in the imported hierarchy.
# So in the case of os.path, it executes os.__init__.py and then path.__init__.py

import os.path as pth  # only import os.path module. os module need to be imported separately.
# note both os and path __init__.py files will still be run.
