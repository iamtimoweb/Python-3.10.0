"""
The for statement in Python has the ability to iterate over the items of any sequence, such
as a list or a string.
"""
fruits = ['mangoes', 'oranges', 'coconuts', 'pineapples']

for fruit in fruits:
    print('The fruit is: ' + fruit)

"""
The range() function: The built-in function range() is the right function to iterate over a sequence of numbers. 
It generates an iterator of arithmetic progressions.

To obtain a list object of the sequence, it is typecasted to list(). Now this list can be iterated using the 
for statement.
"""

# range() generates an iterator to progress integers starting with 0 upto n-1.
numbers = list(range(20))
for num in numbers:
    print(str(num) + ' ', end='')
print('Good bye')

"""
Iterating by Sequence Index: An alternative way of iterating through each item is by index offset into the sequence 
itself.
"""
for index in range(len(fruits)):
    print('Current fruit :', fruits[index])
print("Good bye!")

numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]
for num in numbers:
    if num % 2 == 0:
        print('the list contains an even number')
    break
else:
    print('the list does not contain even number')
