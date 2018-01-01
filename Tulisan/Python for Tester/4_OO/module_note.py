"""How to use module
Modules are simply source files, ending in .py and located somewhere that Python can find them.
(the file must be located in the current working directory or a folder listed in the sys.path variable)

When you enter an import command and the name of the module, Python checks the
following locations in the order shown here:

1.  The home directory — This is either the directory from which you launched the Python
interactive interpreter or the directory where your main program is located.
2.  PYTHONPATH — This is an environment variable set in the system. Its value is a list of
directories, which Python will search for modules.
3.  Standard library directories — The directory in which the standard libraries are located are
searched next.

avoid top-level code that will be run when the module is imported, except, possibly,
for some initialization of variables that may depend on the local environment. This means that the code
you want to reuse should be packaged as a function or a class.




import forms are:

import aModule
import aModule as anAlias
import firstModule, secondModule, thirdModule...  # not recommended

from aModule import anObject
from aModule import anObject as anAlias

from aModule import firstObject,secondObject, thirdObject...  # also not recommended

from aModule import *  # imports all the visible names from aModule into the current namespace.
# have risk of naming conflicts with built-in names or names you have defined, or will define, locally.

"""

__all__ = ['bar', 'TestModule']  # see import_all.py for definition and usage
# names to export. Only these two get imported by 'from foo import *'

wah = 5
bar = 10
_a_global_var = 2  # single leading underscore so it won't get imported by 'from foo import *'
_b_global_var = 3


class TestModule(object):

    def baz(self): return 'baz yeah'


if __name__ == '__main__':
    """best practice: provide a test  function that exercises all the functions and classes in the module."""
    tm = TestModule()
    assert tm.baz() == 'baz yeah!'
