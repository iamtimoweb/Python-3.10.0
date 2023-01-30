"""
An exception is an event, which occurs during the execution of a program that disrupts
the normal flow of the program's instructions. In general, when a Python script encounters
a situation that it cannot cope with, it raises an exception. An exception is a Python object
that represents an error.

When a Python script raises an exception, it must either handle the exception immediately
otherwise it terminates and quits.
"""
"""
Handling an Exception
===============================================================================================
If you have some suspicious code that may raise an exception, you can defend your 
program by placing the suspicious code in a try: block. After the try: block, include 
an except: statement, followed by a block of code which handles the problem as elegantly 
as possible

SYNTAX
=================
try:
    You do your operations here
    ...........................
except ExceptionI:
    If there is ExceptionI, then execute this block.
    ...........................
except ExceptionII:
    If there is ExceptionII, then execute this block.
    ...........................
else:
   If there is no exception then execute this block.
   
The except Clause with No Exceptions
===============================================================================================
This kind of a try-except statement catches all the exceptions that occur. Using this kind 
of try-except statement is not considered a good programming practice though, because 
it catches all exceptions but does not make the programmer identify the root cause of the 
problem that may occur.

try:
    You do your operations here
    ......................
except:
    If there is any exception, then execute this block.
    ......................
else:
    If there is no exception then execute this block.
    
The except Clause with Multiple Exceptions
===============================================================================================
You can also use the same except statement to handle multiple exceptions as follows:

try:
    You do your operations here
 ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
    If there is any exception from the given exception list,
    then execute this block.
    ......................
else:
    If there is no exception then execute this block.
"""
try:
    fh = open("./testfile.txt", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

"""
===============================ANOTHER EXAMPLE========================================
"""
try:
    fh = open("testfile.pdf", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file with the extension of .pdf or read data from it")
else:
    print("Written content in the file successfully")
