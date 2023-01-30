import time
import calendar

"""
Number of seconds from 1st January 1970 (Epoch time)
"""
print("The current time in seconds since 1st january 1970: ", time.time())

"""
The current time represented as time-tuple with all valid nine items.
"""
print("Current time represented as a time-tuple with valid nine items: ", time.localtime())

"""
=================================Getting formatted time===============================
"""
# You can format any time as per your requirement, but a simple method to get time in a
# readable format is asctime()
print("Time now is: ", time.asctime())

"""
==================================Getting calendar for a month=========================
"""
calendar__for__october = calendar.month(2022, 10)
print(calendar__for__october)

"""
The method ctime() converts a time expressed in seconds since the epoch to a string 
representing local time. If secs is not provided or None, the current time as returned by 
time() is used.
"""
print("ctime : ", time.ctime(), type(time.ctime()))
