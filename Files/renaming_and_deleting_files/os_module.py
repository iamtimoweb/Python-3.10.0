import os

"""
Python os module provides methods that help you perform file-processing operations, 
such as renaming and deleting files.
"""

"""
The rename() Method:
=======================================================================================================================
Takes two arguments, the current filename and the new filename.
"""
try:
    os.rename('../sample_files/text_file.txt', '../sample_files/text_file.txt')
except FileNotFoundError:
    print('Cannot find the file specified')
else:
    print('The file has been renamed successfully')

"""
The remove() Method
======================================================================================================================
You can use the remove() method to delete files by supplying the name of the file to be 
deleted as the argument.
"""
try:
    os.remove('../sample_files/text_file.txt')
except FileNotFoundError:
    print('Cannot find the file specified')
else:
    print('The file has been renamed successfully')

"""
************************************** DIRECTORIES IN PYTHON ==========================================================
All files are contained within various directories, and Python has no problem handling these 
too. The os module has several methods that help you create, remove, and change 
directories.
"""
"""
The mkdir() Method
=======================================================================================================================
You can use the mkdir() method of the os module to create directories in the current 
directory. You need to supply an argument to this method, which contains the name of 
the directory to be created.
"""
try:
    os.mkdir('genius')
except FileExistsError:
    print('Directory already exists')
else:
    print('Directory created successfully')

"""
The chdir() Method
=======================================================================================================================
You can use the chdir() method to change the current directory. The chdir() method takes 
an argument, which is the name of the directory that you want to make the current 
directory.
"""
# Changing a directory to "./genius"
os.chdir("./genius")

"""
The getcwd() Method
=======================================================================================================================
The getcwd() method displays the current working directory.
"""
print(os.getcwd())

"""
The rmdir() Method
======================================================================================================================
The rmdir() method deletes the directory, which is passed as an argument in the method.
Before removing a directory, all the contents in it should be removed.
"""
try:
    os.rmdir('../sports')
except FileNotFoundError:
    print('The system cannot find the file specified')
else:
    print("File removed successfully")
