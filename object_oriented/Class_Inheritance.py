"""
Instead of starting from a scratch, you can create a class by deriving it from a pre-existing
class by listing the parent class in parentheses after the new class name.

The child class inherits the attributes of its parent class, and you can use those attributes
as if they were defined in the child class. A child class can also override data members and
methods from the parent.
"""


class Parent:
    parent_attr = 100

    def __init__(self):
        print("calling the parent constructor")

    @staticmethod
    def parent_method():
        print('Calling parent method')

    @staticmethod
    def set_attr(attr):
        Parent.parent_attr = attr

    @staticmethod
    def get_attr():
        print("Parent attribute :", Parent.parent_attr)


class Child(Parent):
    pass


obj_child = Child()  # instance of child
obj_child.parent_method()  # calls parent's method
obj_child.set_attr(200)  # again call parent's method
obj_child.get_attr()  # again call parent's method

# performing some checks using the isSubclass or isInstance methods
print("The Child class is a subclass of Parent class: ", issubclass(Child, Parent))
print("obj_child is an instance of the Child class", isinstance(obj_child, Child))
print("obj_child is an instance of the Parent class", isinstance(obj_child, Parent))

obj_parent = Parent()
print("The Parent class is a subclass of Child class: ", issubclass(Parent, Child))
print("obj_parent is an instance of the Parent class", isinstance(obj_parent, Parent))
print("obj_parent is an instance of the Child class", isinstance(obj_parent, Child))

"""======In a similar way, you can drive a class from multiple parent classes as follows======
class A: # define your class A
.....
class B: # define your class B
.....
class C(A, B): # subclass of A and B
"""
