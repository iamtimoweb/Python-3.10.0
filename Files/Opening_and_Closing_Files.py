# opening a file and creating a file object
file_object = ''
try:
    file_object = open("./sample_files/text_file.txt", 'r')
except FileNotFoundError:
    print('NO such file or directory')
else:
    print("The name of the file is: ", file_object.name)
    print("Is the file closed or not:", file_object.closed)
    print("The opening mode of the file is: ", file_object.mode)

    file_object.close()
    print("=================================================")
    print("The file is now closed:", file_object.closed)

"""
Reading and Writing Files
=================================================================================================================
The file object provides a set of access methods to make our lives easier. We would see how to use read() and write() methods to read and write files respectively.
"""

"""
The write() Method: 
==================================================================================================================
The write() method writes any string to an open file. It is important to note that Python
strings can have binary data and not just text.

Note: The write() method does not add a new line character to the end of the string.
"""
f_obj = open('./sample_files/my_name.txt', 'w')

# writing to the opened file
f_obj.write('My name is Timo Web and I love python and django framework')

# close the opened file
f_obj.close()

"""
The read() Method
====================================================================================================================
The read() method reads a string from an open file. It is important to note that Python 
strings can have binary data apart from the text data.

SYNTAX: fileObject.read([count])
Here, passed parameter is the number of bytes to be read from the opened file. This 
method starts reading from the beginning of the file and if count is missing, then it tries 
to read as much as possible, maybe until the end of file.
"""
f_ob = open('./sample_files/my_name.txt', 'r+')
try:
    str_from_file = f_ob.read(58)
except FileNotFoundError:
    print('No such file or directory')
else:
    print("The text from the file is: ", str_from_file)

# Check current position using the tell() method
position = f_ob.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = f_ob.seek(0, 0)
str_from_file = f_ob.read(10)
print("Again the text from the file is : ", str_from_file)

# More File Methods
"""Returns the integer file descriptor that is used by the underlying implementation 
to request I/O operations from the operating system.
"""
print("file.fileno", f_ob.fileno())
print("file.isatty()", f_ob.isatty())
f_ob.close()
