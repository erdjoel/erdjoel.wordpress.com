"""
NOTE: __all__ in import_module.py affects the from <module> import * behavior only.
Members that are not mentioned in __all__ are still accessible from outside the module
and can be imported with from <module> import <member>.

default behaviour of import * is to import all symbols that do not begin with an underscore, from the given namespace.
"""
from module_note import *

print('test')
# The following will work as expected, because bar and baz is imported

print(bar)

tm = TestModule()
print(tm.baz())

print(wah)  # not imported

# The following will trigger an exception, as "waz" is not exported by the module
# print(module_note.TestModule.wah)
