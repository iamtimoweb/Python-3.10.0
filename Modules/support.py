import python_modules
from module_2 import add

"""Print my name"""
python_modules.print_name('Jenkins')

"""
The from...import Statement
===================================================================================================================
Python's from statement lets you import specific attributes from a module into the current 
namespace.
"""
add(80, 150)

"""
The from...import * Statement:
==================================================================================================================
It is also possible to import all the names from a module into the current namespace by 
using the following import statement.

-------------from modname import * -----------------------
This provides an easy way to import all the items from a module into the current 
namespace; however, this statement should be used sparingly.
"""

"""
Executing Modules as Scripts
===================================================================================================================
Within a module, the module’s name (as a string) is available as the value of the global 
variable __name__. The code in the module will be executed, just as if you imported it, 
but with the __name__ set to "__main__".
"""

