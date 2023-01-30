"""
An assertion is a sanity-check that you can turn on or turn off when you are done with
your testing of the program.

 The easiest way to think of an assertion is to liken it to a raise-if statement (or to
  be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised
"""
"""
Here is a function that converts a given temperature from degrees Kelvin to degrees 
Fahrenheit. Since 0° K is as cold as it gets, the function bails out if it sees a negative 
temperature
"""


def kelvin_to_fahrenheit(temperature):
    assert (temperature > 0), "colder than absolute zero"
    return ((temperature - 273) * 1.8) + 32


print("The temperature 273 in fahrenheit is now: ", kelvin_to_fahrenheit(273))
print("The temperature 505.78 in fahrenheit is now: ", kelvin_to_fahrenheit(505.78))
print("The temperature -5 in fahrenheit is now: ", kelvin_to_fahrenheit(-5))
