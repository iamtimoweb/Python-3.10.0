"""
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
"""

a = 10
b = 20
mylist = [1, 2, 3, 4, 5]

if a in mylist:
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if b not in mylist:
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

c = b / a
if c in mylist:
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")
