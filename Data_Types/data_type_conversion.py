"""
Sometimes, you may need to perform conversions between the built-in types.
To convert between types, you simply use the type-name as a function.
There are several built-in functions to perform conversion from one data type to another.
These functions return a new object representing the converted value.
"""

"""
int(x [,base]) - Converts x to an integer. The base specifies the base if x is a string.
float(x) - Converts x to a floating-point number.
complex(real [,imag]) - Creates a complex number.

str(x) - Converts object x to a string representation.
repr(x) - Converts object x to an expression string.
eval(str) - Evaluates a string and returns an object.
tuple(s) - Converts s to a tuple.
list(s) - Converts s to a list.
set(s) - Converts s to a set.
dict(d) - Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) - Converts s to a frozen set.
chr(x) - Converts an integer to a character.
unichr(x) - Converts an integer to a Unicode character.
ord(x) - Converts a single character to its integer value.
hex(x) - Converts an integer to a hexadecimal string.
oct(x) - Converts an integer to an octal string."""

mystring = 'Hello world'
print(list(mystring), ' is of type ', type(list(mystring)))

print(oct(num))
print(chr(num))
