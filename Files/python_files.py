# Printing to the screen
print("Python is really a great language")

# Reading the keyboard input
"""Python 2 has two built-in functions to read data from standard input. These functions are input() and raw_input()"""

"""In Python 3, raw_input() function is deprecated. Moreover, input() functions read data 
from keyboard as string, irrespective of whether it is enclosed with quotes ('' or "" ) or 
not."""

x = input("Please enter a value: \n")
print("The value you entered is {} and is of type".format(x), " and is of type ", type(x))

"""
=====================================Opening and Closing Files============================================
Python provides basic functions and methods necessary to manipulate files by default. You 
can do most of the file manipulation using a file object.
"""
# The open Function: Before you can read or write a file, you have to open it using Python's built-in open() function. This function creates a file object, which would be utilized to call other support methods associated with it.
"""
file object = open(file_name [, access_mode][, buffering])

 file_name: The file_name argument is a string value that contains the name of 
              the file that you want to access.
              
 access_mode: The access_mode determines the mode in which the file has to be 
                opened, i.e., read, write, append, etc. A complete list of possible values is given 
                below in the table. This is an optional parameter and the default file access mode 
                is read (r).
                
 buffering: If the buffering value is set to 0, no buffering takes place. If the 
              buffering value is 1, line buffering is performed while accessing a file. If you specify 
              the buffering value as an integer greater than 1, then buffering action is performed 
              with the indicated buffer size. If negative, the buffer size is the system default (default behavior).

"""
