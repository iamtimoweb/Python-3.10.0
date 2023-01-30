"""
An object's attributes may or may not be visible outside the class definition. You need to
name attributes with a double underscore prefix, and those attributes then will not be
directly visible to outsiders.
"""


class JustCounter:
    # Visible only inside this class
    __secret_count = 0

    def __init__(self):
        JustCounter.__secret_count = JustCounter.__secret_count + 1

    def display_count(self):
        print("The count is: ", self.__secret_count)


obj_1 = JustCounter()
obj_1.display_count()

obj_2 = JustCounter()
obj_2.display_count()
