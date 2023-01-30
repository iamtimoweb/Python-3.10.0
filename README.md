# Python-3.10.0
Python is a programming language that lets you work quickly and integrate systems more effectively.

# Quick & Easy to Learn
Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. Whet your appetite with our Python 3 overview.

```python
# Simple output (with Unicode)
>>> print("Hello, I'm Python!")
Hello, I'm Python!
# Input, assignment
>>> name = input('What is your name?\n')
What is your name?
Python
>>> print(f'Hi, {name}.')
Hi, Python.
```

# Compound Data Types
Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions

```python
# Python 3: List comprehensions
>>> fruits = ['Banana', 'Apple', 'Lime']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
['BANANA', 'APPLE', 'LIME']

# List and the enumerate function
>>> list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]
```

# Functions Defined
The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists.

```python

"""
A function is a block of organized, reusable code that is used to perform a single, related
action.Functions provide better modularity for your application and a high degree of code
reusing.
"""

"""
Defining a Function
________________________________________________________________________________________________________
You can define functions to provide the required functionality. Here are simple rules to define a function in Python.
     Function blocks begin with the keyword def followed by the function name and parentheses (( )).
    
     Any input parameters or arguments should be placed within these parentheses. You can also define parameters      inside these parentheses.
    
     The first statement of a function can be an optional statement - the documentation string of the function or     docstring.
    
     The code block within every function starts with a colon (:) and is indented.
    
     The statement return [expression] exits a function, optionally passing back an expression to the caller. 
      A return statement with no arguments is the same as return None.
"""


# function that takes in a string as an input parameter and prints it on the standard screen

def print_name(name):
    """This prints a passed string into this function"""
    print('Your name is %s' % name)


print_name('Mugabi Timothy')

"""
Pass by Reference vs Value
-------------------------------------------------------------------------------------------------------------
All parameters (arguments) in the Python language are passed by reference. It means if 
you change what a parameter refers to within a function, the change also reflects back in 
the calling function.
"""


def change_me(mylist):
    """This changes a passed list into this function"""
    print("Values inside the function before change: ", mylist)
    mylist[2] = 50
    print("Values inside the function after change: ", mylist)


change_me([10, 'James', 90])

"""
Overriding the reference inside the function
-----------------------------------------------------------------------------------------------------------------
There is one more example where argument is being passed by reference and the 
reference is being overwritten inside the called function.
"""


def override_reference_inside_the_function(mylist):
    """This changes a passed list into this function"""
    mylist = [1, 2, 3, 4]
    print("Overriden Values inside the function: ", mylist)
    return


mylist = [10, 20, 30]
override_reference_inside_the_function(mylist)
print("The values outside the function are {}".format(mylist))

"""
Required Arguments
-------------------------------------------------------------------------------------------------------------------
Required arguments are the arguments passed to a function in correct positional order. 
Here, the number of arguments in the function call should match exactly with the function 
definition.
"""


def print_employee_details(name, age):
    print('The employee name is %s and he or she is %d years old' % (name, age))


print_employee_details('Nankya Shamim', 21)

"""
Keyword Arguments
-----------------------------------------------------------------------------------------------------------------
Keyword arguments are related to the function calls. When you use keyword arguments in a function call, 
the caller identifies the arguments by the parameter name.

This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters.
"""


def student(name, age, nationality):
    return "my name is {} and am {} years old and born in {}".format(name, age, nationality)


result = student(nationality='Ugandan', name='Michael', age=25)
print(result)

"""
Default Arguments
------------------------------------------------------------------------------------------------------------------
A default argument is an argument that assumes a default value if a value is not provided 
in the function call for that argument.
"""


def print_info(name, age=35):
    """This prints a passed info into this function"""
    print("Employee name= %s and Age= %d" % (name, age))


print_info('Ndawula Charles')

"""
Variable-length Arguments
===============================================================================================================
You may need to process a function for more arguments than you specified while defining 
the function. These arguments are called variable-length arguments and are not named in 
the function definition, unlike required and default arguments.

An asterisk (*) is placed before the variable name that holds the values of all nonkeyword 
variable arguments. This tuple remains empty if no additional arguments are specified 
during the function call.
"""


def student_grades(grade, *args):
    """Prints the variable passed arguments"""
    print("Grade is= %s" % grade)
    print('The variable Arguments are: ', end='')
    for arg in args:
        print(arg, end=''.join(', '))


student_grades('B', 40, 50, 60, 70)

"""
The Anonymous Functions
==================================================================================================================
These functions are called anonymous because they are not declared in the standard 
manner by using the def keyword. You can use the lambda keyword to create small 
anonymous functions.

 Lambda forms can take any number of arguments but return just one value in the 
  form of an expression. They cannot contain commands or multiple expressions.
  
 An anonymous function cannot be a direct call to print because lambda requires an 
  expression.
  
 Lambda functions have their own local namespace and cannot access variables 
  other than those in their parameter list and those in the global namespace.
  
 Although it appears that lambdas are a one-line version of a function, they are not 
  equivalent to inline statements in C or C++, whose purpose is to stack allocation
  by passing function, during invocation for performance reasons.
"""
get_sum = lambda x, y: x + y

# Now you can call the sum variable as function
print()
print("The summation of the numbers is %d" % get_sum(60, 40))

"""
The return Statement
=================================================================================================================
The statement return [expression] exits a function, optionally passing back an expression 
to the caller. A return statement with no arguments is the same as return None.
"""


def get_sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


# Now you can call sum function
get_total = get_sum(10, 20)
print("Outside the function : ", get_total)


```
