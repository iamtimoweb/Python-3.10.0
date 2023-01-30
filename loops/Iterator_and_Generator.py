import sys

mylist = [1, 2, 3, 4]
it = iter(mylist)  # this builds an iterator object
print(next(it))  # prints next available element in iterator 

"""
Iterator is an object, which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation. In Python, an iterator object implements two methods, iter() and next().
Iterator object can be traversed using regular for statement
"""

for x in it:
    print(x, end=" ")

# or using next() function

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()  # you have to import sys module for this




