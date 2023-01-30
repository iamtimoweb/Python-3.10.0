# Strings in Python are identified as a contiguous set of characters represented in the quotation marks either double or single quotes
import base64

myString = "Hello World"

"""
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the 
beginning of the string and working their way from -1 to the end.

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition 
operator.
"""
print(myString)  # Prints complete string
print(myString[0])  # Prints first character of the string
print(myString[2:5])  # Prints characters starting from 3rd to 5th
print(myString[2:])  # Prints string starting from 3rd character
print(myString * 2)  # Prints string two times
print(myString + "TEST")  # Prints concatenated string

# String Formatting Operator
print("My name is %s and weight is %d kg!, I obtained 70%% in physics" % ('Zara', 21))

"""
==========================================Built-in String Methods==============================================
"""
# It returns a copy of the string with only its first character capitalized.
myString = 'hello world'
print("str.capitalize() : ", myString.capitalize())

# This method returns a string that is at least width characters wide, created by padding the
# string with the character fillchar (default is a space).
string = "this is string example....wow!!!"
print("str.center(40, 'a') : ", string.center(40, 'a'))

"""
The count() method returns the number of occurrences of substring sub in the range 
[start, end]. Optional arguments start and end are interpreted as in slice notation.
"""
string = "this is string example....wow!!!"
sub = 'i'
print("str.count('i') : ", string.count(sub))
sub = 'exam'
print("str.count('exam', 10, 40) : ", string.count(sub, 10, 40))

"""
The decode() method decodes the string using the codec registered for encoding. It 
defaults to the default string encoding.

Syntax: Str.decode(encoding='UTF-8',errors='strict')

Parameters
     encoding - This is the encodings to be used. For a list of all encoding schemes please visit: Standard Encodings.
     errors - This may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error()..
"""
String = "this is string example....wow!!!"
String = base64.b64encode(String.encode('utf-8', errors='strict'))
print("Encoded String: ", String)
print("Decoded String: ", base64.b64decode(String.decode('utf-8', errors='strict')))

# String encode() Method
"""
The encode() method returns an encoded version of the string. Default encoding is the 
current default string encoding. The errors may be given to set a different error handling scheme.
"""
String = "this is string example....wow!!!"
String = base64.b64encode(String.encode('utf-8', errors='strict'))
print("Encoded String: ", String)

# MORE METHODS
"""

capitalize() - Capitalizes first letter of string

center(width, fillchar) - Returns a string padded with fillchar with the original string centered to a total
                          of width columns.

count(str, beg= 0,end=len(string)) - Counts how many times str occurs in string or in a substring of string if starting 
                                     index beg and ending index end are given.

decode(encoding='UTF-8',errors='strict') - Decodes the string using the codec registered for encoding. encoding defaults 
                                           to the default string encoding.

encode(encoding='UTF-8',errors='strict') - Returns encoded string version of string; on error, default is to raise a 
                                           ValueError unless errors is given with 'ignore' or 'replace'.

endswith(suffix, beg=0, end=len(string) - Determines if string or a substring of string (if starting index beg and ending 
                                          index end are given) ends with suffix; returns true if so and false otherwise.

expandtabs(tabsize=8) - Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize 
                        not provided.

find(str, beg=0 end=len(string)) - Determine if str occurs in string or in a substring of string if starting index beg 
                                   and ending index end are given returns index if found and -1 otherwise.

index(str, beg=0, end=len(string)) - Same as find(), but raises an exception if str not found.

isalnum() - Returns true if string has at least 1 character and all characters are 
            alphanumeric and false otherwise.

isalpha() - Returns true if string has at least 1 character and all characters are alphabetic 
            and false otherwise.

isdigit() - Returns true if the string contains only digits and false otherwise.

islower() - Returns true if string has at least 1 cased character and all cased characters are in lowercase 
            and false otherwise.

isnumeric() - Returns true if a unicode string contains only numeric characters and false otherwise.

isspace() - Returns true if string contains only whitespace characters and false otherwise.

istitle() - Returns true if string is properly "title cased" and false otherwise.

isupper() - Returns true if string has at least one cased character and all cased characters are in uppercase 
            and false otherwise.

join(seq) - Merges (concatenates) the string representations of elements in sequence seq 
            into a string, with separator string.
            
len(string) - Returns the length of the string

ljust(width[, fillchar]) - Returns a space-padded string with the original string left-justified to a total 
                           of width columns.

lower() - Converts all uppercase letters in string to lowercase.

lstrip() - Removes all leading whitespace in string.

maketrans() - Returns a translation table to be used in translate function.

max(str) - Returns the max alphabetical character from the string str.

min(str) - Returns the min alphabetical character from the string str.

replace(old, new [, max]) - Replaces all occurrences of old in string with new or at most max occurrences if max given.

rfind(str, beg=0,end=len(string)) - Same as find(), but search backwards in string.

rindex( str, beg=0, end=len(string)) - Same as index(), but search backwards in string.

rjust(width,[, fillchar]) - Returns a space-padded string with the original string right-justified to a total of width columns.

rstrip() - Removes all trailing whitespace of string.

split(str="", num=string.count(str)) - Splits string according to delimiter str (space if not provided) and returns list 
                                       of substrings; split into at most num substrings if given.

splitlines( num=string.count('\n')) - Splits string at all (or num) NEWLINEs and returns a list of each line with 
                                      NEWLINEs removed.
                                
startswith(str, beg=0,end=len(string)) - Determines if string or a substring of string (if starting index beg and ending 
                                         index end are given) starts with substring str; returns true if so and false otherwise.

strip([chars]) - Performs both lstrip() and rstrip() on string

swapcase() - Inverts case for all letters in string.

title() - Returns "title cased" version of string, that is, all words begin with uppercase and the rest are lowercase.

translate(table, deletechars="") -Translates string according to translation table str(256 chars), removing those 
in the del string.

upper() - Converts lowercase letters in string to uppercase.

zfill (width) - Returns original string left padded with zeros to a total of width characters; intended for numbers, zfill()                      retains any sign given (less one zero).

isdecimal() - Returns true if a unicode string contains only decimal characters and false otherwise.

"""

NAME = "Mugabi timothy"
NUM = str('09876')
print("islower()", NAME.lower().islower())
print("isupper()", NAME.upper().isupper())
print("isdigit()", NUM.isdigit())
