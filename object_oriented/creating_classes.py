class Employee:
    """This is an Employee class"""

    # class variable whose value is shared among all the instances of this class
    empCount = 0

    # creating instance variables using the init or constructor function
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount = Employee.empCount + 1

    @staticmethod
    def display_count():
        print("The total number of employees is: ", Employee.empCount)

    def display_employee(self):
        print("Employee Name: %s, Employee Salary: %d " % (self.name, self.salary))


"""====================================Creating Instance Objects============================="""

# This would create first object of Employee class
emp1 = Employee("Zara", 2000)

# This would create second object of Employee class
emp2 = Employee("Manni", 5000)

"""=====================================Accessing Attributes================================="""
emp1.display_employee()
emp2.display_employee()

# Tracking the number of employee created for the class
print("Total Employee: %d" % Employee.empCount)

# You can add, remove, or modify attributes of classes and objects at any time
emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'Mabirizi'  # Modify 'name' attribute.

# Now print again the emp1 details to reflect new changes
# emp1.display_employee()

# Instead of using the normal statements to access attributes, you can use the following
# functions-
print("The new salary for employee 1 is: ", getattr(emp1, 'salary'))

print("The new salary for employee 2 will be: ", setattr(emp2, 'salary', 8000))
print("Emp 2 has attribute salary: ", hasattr(emp2, 'salary'))

delattr(emp1, 'salary')  # Delete attribute 'age'
print("Emp 1 has attribute salary: ", hasattr(emp1, 'salary'))

"""===============================Built in class attributes================================="""
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
