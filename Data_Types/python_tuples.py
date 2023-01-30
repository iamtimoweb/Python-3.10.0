"""
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
The main difference between the tuples and the lists is that the tuples cannot be changed
unlike lists. Tuples use parentheses, whereas lists use square brackets.
 """
mytuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

"""
The main difference between lists and tuples is- Lists are enclosed in brackets ( [ ] ) and 
their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) 
and cannot be updated. Tuples can be thought of as read-only lists.
"""
print(mytuple)  # Prints complete tuple
print(mytuple[0])  # Prints first element of the tuple
print(mytuple[1:3])  # Prints elements starting from 2nd till 3rd
print(mytuple[2:])  # Prints elements starting from 3rd element
print(tinytuple * 2)  # Prints tuple two times
print(mytuple + tinytuple)  # Prints concatenated tuple

"""
Updating Tuples: Tuples are immutable, which means you cannot update or change the values of tuple 
elements. You are only able to take portions of the existing tuples to create new tuples
"""
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

"""
Following action is not valid for tuples 
tup1[0] = 100
"""

"""So let's create a new tuple as follows"""
tup3 = tup1 + tup2
print("The new tuple created is: ", tup3)

# Delete Tuple Elements
"""
Removing individual tuple elements is not possible. There is, of course, nothing wrong with 
putting together another tuple with the undesired elements discarded.
del tup[3]
"""
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
# print("After deleting tup : ", tup) raises an error of tup is not defined.

"""
==========================================TUPLE FUNCTIONS AVAILABLE IN PYTHON========================================
"""
# The len() function returns the number of elements in the tuple.
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print("First tuple length : ", len(tuple1))
print("Second tuple length : ", len(tuple2))

# The max() function returns the elements from the tuple with maximum value.
tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)
print("Max value element : ", max(tuple1))
print("Max value element : ", max(tuple2))

# This function returns the elements from the tuple with minimum value.
print("min value element : ", min(tuple1))
print("min value element : ", min(tuple2))

# This function returns the tuple.
list1 = ['maths', 'che', 'phy', 'bio']
tuple1 = tuple(list1)
print("tuple elements : ", tuple1)


