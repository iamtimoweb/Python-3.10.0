"""
Lists are the most versatile of Python's compound data types. A list contains items
separated by commas and enclosed within square brackets ([]).
"""

mylist = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

"""
To some extent, lists are similar to arrays in C. One of the differences between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with 
indexes starting at 0 in the beginning of the list and working their way to end -1. The plus 
(+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. 
"""
print(mylist)  # Prints complete list
print(mylist[0])  # Prints first element of the list
print(mylist[1:3])  # Prints elements starting from 2nd till 3rd
print(mylist[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(mylist + tinylist)  # Prints concatenated lists

# Deleting a list
del mylist[2]
print(mylist)  # Prints complete list after deletion
"""
====================================LIST FUNCTIONS AVAILABLE IN PYTHON=================
"""
# finding the length of a list
print('The list length is: ', len(mylist))

# finding the maximum value from the list elements
list1, list2 = ['C++', 'Java', 'Python'], [456, 700, 200]
print("Max value element : ", max(list1))
print("Max value element : ", max(list2))

# minimum value
print("min value element : ", min(list1))
print("min value element : ", min(list2))

# converting a string or tuple in a list
aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print("List elements : ", list1)
str_ = "Hello World"
list2 = list(str_)
print("List elements : ", list2)

"""
==========================================LIST METHODS AVAILABLE IN PYTHON=========================================
"""
# The append() method appends a passed obj into the existing list.
list2 = ['C++', 'Java', 'Python']
list2.append('C#')
print("updated list : ", list2)

# The count() method returns count of how many times obj occurs in list.
aList = [123, 'xyz', 'zara', 'abc', 123];
print("Count for 123 : ", aList.count(123))
print("Count for zara : ", aList.count('zara'))

# This method does not return any value but adds the content to an existing list.
list1 = ['physics', 'chemistry', 'maths']
list2 = list(range(5))  # creates list of numbers between 0-4
list1.extend(list2)
print('Extended List :', list1)

# This method returns index of the found object otherwise raises an exception indicating that the value is not found.
list1 = ['physics', 'chemistry', 'maths']
print('Index of chemistry', list1.index('chemistry'))
# print('Index of C#', list1.index('C#')) raises an exception since the value of C# is not present from the list

# This method does not return any value but it inserts the given element at the given index.
list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'Biology')
print('Final list : ', list1)

# This method returns the removed object from the list.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print('The removed element from the list is: ', list1.pop())
print("list now : ", list1)
print('The removed element from the list is: ', list1.pop(1))
print("list now : ", list1)

# This method does not return any value but removes the given object from the list.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.remove('Biology')
print("list now : ", list1)
list1.remove('maths')
print("The new list now : ", list1)

# The reverse() method reverses objects of list in place.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.reverse()
print("list now when reversed is : ", list1)

# This method does not return any value but reverses the given object from the list.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print("The sorted list now : ", list1)
