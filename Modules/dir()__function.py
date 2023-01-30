"""
The dir() built-in function returns a sorted list of strings containing the names defined by a module.

The list contains the names of all the modules, variables and functions that are defined in a module.
"""

import math
import time



"""
print all te names of variables, functions, modules contained in the math module
"""
module_math = dir(math)
print(module_math)

print("=======================================================================================================")
"""
print all te names of variables, functions, modules contained in the time module
"""
module_time = dir(time)
print(module_time)
