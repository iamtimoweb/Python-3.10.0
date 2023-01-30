"""
A loop becomes infinite loop if a condition never becomes FALSE. You must be cautious
when using while loops because of the possibility that this condition never resolves to a
FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop.
"""

var = 1
while var == 1:  # This constructs an infinite loop
    num = int(input("Enter a number :"))
    print("You entered: ", num)
print("Good bye!")
