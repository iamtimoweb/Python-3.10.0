import sys

"""
A module allows you to logically organize your Python code.

Grouping related code into a module makes the code easier to understand and use.

A module is a Python object with arbitrarily named attributes that you can bind and reference.
"""

"""
Simply, a module is a file consisting of Python code. 

A module can define functions, classes and variables. A module can also include runnable code.
"""


def print_name(name):
    print('My name is: ', name)


"""
Locating Module
==================================================================================================================
When you import a module, the Python interpreter searches for the module in the following 
sequences-

 The current directory.
 If the module is not found, Python then searches each directory in the shell variable PYTHONPATH.
 If all else fails, Python checks the default path. On UNIX, this default path is 
   normally /usr/local/lib/python3/.
   
The module search path is stored in the system module sys as the sys.path variable. The 
sys.path variable contains the current directory, PYTHONPATH, and the installation - dependent default.
"""

"""
Namespaces and Scoping
===================================================================================================================
Variables are names (identifiers) that map to objects. A namespace is a dictionary of 
variable names (keys) and their corresponding objects (values).
 A Python statement can access variables in a local namespace and in the global 
  namespace. If a local and a global variable have the same name, the local variable 
  shadows the global variable.
  
 Each function has its own local namespace. Class methods follow the same scoping 
  rule as ordinary functions.
  
 Python makes educated guesses on whether variables are local or global. It 
  assumes that any variable assigned a value in a function is local.
  
 Therefore, in order to assign a value to a global variable within a function, you must 
  first use the global statement.
  
 The statement global VarName tells Python that VarName is a global variable. 
  Python stops searching the local namespace for the variable.
"""
money = 2000


def add_money():
    # Note: python assumes that any variable assigned a value in a function is local.
    global money
    money = money + 1
    print("Inside the Function: ", money)


print("The total money is: ", money)
add_money()  # changes the value of money outside the function
print("Outside the function: ", money)

if __name__ == "__main__":
    print_name('Okalebo Frank')
    print("Module Search Path", sys.path)
