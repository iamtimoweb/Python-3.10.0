"""
Python's dictionaries are kind of hash-table type. They work like associative arrays or
hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any
Python type, but are usually numbers or strings. Values, on the other hand, can be any
arbitrary Python object.


"""
mydict = {'one': "This is one", 2: "This is two"}

"""
A dictionary key can be almost any Python type, but are usually numbers or strings. 
Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed 
using square braces ([]).
"""
print(mydict['one'])
print(mydict[2])

"""
Updating Dictionary: You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown in a simple example given below.
"""
# assigning different values to dictionary
mydict['one'] = 'The storm is over'
mydict[2] = 'How to be perfected in God'

print(mydict['one'])
print(mydict[2])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

"""
==============================================Delete Dictionary Elements=============================================
You can either remove individual dictionary elements or clear the entire contents of a 
dictionary. You can also delete entire dictionary in a single operation.
"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']  # remove entry with key 'Name'
dict.clear()  # remove all entries in dict
del dict  # delete entire dictionary

print("dict['Age']: ", dict['Age'])

"""
==================================Properties of Dictionary Keys===========================
Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. However, same is not true for the keys.
"""

"""
More than one entry per key is not allowed. This means no duplicate key is allowed. 
When duplicate keys are encountered during assignment, the last assignment wins. For 
example-
"""
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("Duplicate keys dict['Name']: ", dict['Name'])

"""
Keys must be immutable. This means you can use strings, numbers or tuples as 
dictionary keys but something like ['key'] is not allowed. Following is a simple example

dict = {['Name']: 'Zara', 'Age': 7}
print("dict['Name']: ", dict['Name']) raises a TypeError: unhashable type: 'list'

"""

"""
==============================================Built-in Dictionary Functions=============================================
"""
# len() function: This function returns the length.
dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print("Length of the dictionary : %d" % len(dict))

# Dictionary str() function: This function returns string representation.
dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print("Equivalent String : %s" % str(dict), type(str(dict)))

# Dictionary type() function: This function returns the type of the passed variable
dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print("Variable Type : %s" % type(dict))

"""
===================================Built-in DictionaryMethods================================
"""
# Dictionary clear() Method: The method clear() removes all items from the dictionary.
dict = {'Name': 'Zara', 'Age': 7}
print("Start Len : %d" % len(dict))
dict.clear()  # clears all the items from the dictionary
print("End Len : %d" % len(dict))

# Dictionary copy() Method: The method copy() returns a shallow copy of the dictionary.
dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print("New shallow copy of the dictionary : ", dict2)

# Dictionary fromkeys() Method: The method creates a new dictionary with keys from seq and values set to value.
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("New Dictionary : %s" % dict, type(dict))
dict = dict.fromkeys(seq, 10)
print("New Dictionary : %s" % str(dict), type(str(dict)))

# Dictionary get() Method: returns a value for the given key. If the key is not available, then returns
# default value as None.
"""
dict.get(key, default=None)
Parameters
 key - This is the Key to be searched in the dictionary.
 default - This is the Value to be returned in case key does not exist.
"""
dict = {'Name': 'Zara', 'Age': 27}
print("Value : %s" % dict.get('Age'))
print("Value : %s" % dict.get('Sex', "NA"))

# Dictionary items() Method: returns a list of dict's (key, value) tuple pairs.
dict = {'Name': 'Zara', 'Age': 7}
print("The list of key value pairs from the dictionary is: %s" % dict.items())

# Dictionary keys() Method: Returns a list of all the available keys in the dictionary.
dict = {'Name': 'Zara', 'Age': 7}
print("All the keys available in the dictionary are : %s" % dict.keys())

# Dictionary setdefault() Method: returns the key value available in the dictionary and if given key is not available then it will return provided default value.
"""
The method setdefault() is similar to get(), but will set dict[key]=default if the key is not 
already in dict
"""
dict = {'Name': 'Zara', 'Age': 7}
print("The default Value : %s" % dict.setdefault('Age', None))
print("The default Value : %s" % dict.setdefault('Sex', None))
print("The default Value : %s" % dict.setdefault('Nationality', "Ugandan"))
print(dict)

# Dictionary update() Method:
"""
 Adds dictionary dict2's key-values pairs in to dict. This function does not return anything.
"""
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'}
dict.update(dict2)
print("updated dict : ", dict)

# Dictionary values() Method: This method returns a list of all the values available in a given dictionary.
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print("Values : ", list(dict.values()))
