import os
# importing a class from textfile.py module from employee package
from employee.textfile import TextFile


class Employee:  # class definition
    raise_percent = 25  # class variable
    salary_sum = 0
    file = os.path.join(os.getcwd(), 'Employee.txt')

    # __init__ method is a constructor that gets invoked implicitly during object creation
    # for instance methods - by default self is the first param (similar to that of 'this' in java)
    def __init__(self, first, last, salary, designation):
        print('Constructor invoked for Employee class')
        self.tf = TextFile()  # object creation for imported class
        self.tf.txt = ''
        self.first = first
        self.last = last
        self.salary = salary
        self.designation = designation
        self.fullname()
        self.email()
        self.basic_calc()
        self.revised_sal_calc()
        self.tf.file_append(Employee.file)

    def fullname(self):  # instance method to print full name
        print('Employee name = {} {}'.format(self.first, self.last))
        self.tf.txt += 'Employee name = {} {}\n'.format(self.first, self.last)

    def email(self):  # instance method to print email
        email = (self.first + '.' + self.last + '@abc.com').lower()
        print('Email = {}'.format(email))
        self.tf.txt += 'Email = {}\n'.format(email)

    def basic_calc(self):  # instance method to calculate the basic component
        basic = (40 * self.salary) / 100
        print('Basic component = ', basic)
        self.tf.txt += 'Basic component = {}\n'.format(basic)

    def revised_sal_calc(self):
        # instance method to calculate revised_salary based on derived raise_percentage
        actual_raise = Employee.raise_per_calc(self.designation)
        rev_salary = self.salary + (self.salary * actual_raise) / 100
        print('The Revised salary = {}'.format(rev_salary))
        self.tf.txt += 'The Revised salary = {}\n'.format(rev_salary)

        Employee.salary_sum += rev_salary
        print('The salary_sum of Employee class = {}'.format(Employee.salary_sum))
        Employee.salary_slab(rev_salary)
        self.tf.txt += 'The salary_sum of Employee class = {}\n------\n'.format(Employee.salary_sum)
        print('self.tf.txt = ', self.tf.txt)

    @classmethod
    def raise_per_calc(cls, designation):
        # class method to calculate actual_raise based on designation and raise_percent
        if designation == 'Manager' or designation == 'Senior Manager':
            actual_raise = Employee.raise_percent + 15
        else:
            actual_raise = Employee.raise_percent
        print('Designation = ', designation)
        print('Actual raise % = ', actual_raise)
        return actual_raise

    @staticmethod
    def raise_per_calc2(designation):
        """
        alternate method to the aforementioned class method
        to show that class variables can be used within a static method
        Try using this method in the line # 139
        """
        if designation == 'Manager' or designation == 'Senior Manager':
            actual_raise = Employee.raise_percent + 15
        else:
            actual_raise = Employee.raise_percent
        print('The actual raise % =', actual_raise)
        return actual_raise

    @staticmethod
    def salary_slab(salary):
        if salary in range(1, 300001):
            slab = 'S1'
        elif salary in range(300001, 500001):
            slab = 'S2'
        elif salary in range(500001, 800001):
            slab = 'S3'
        elif salary in range(800001, 1000001):
            slab = 'S4'
        else:
            slab = 'S5'

        print('Salary slab of the employee = {}\n-----------'.format(slab))


TextFile.file_clear(Employee.file)
# instantiation/object creation for Employee class
emp1 = Employee('Michael', 'Schofield', 100000, 'Manager')
emp2 = Employee('John', 'Wick', 300000, 'Architect')
emp3 = Employee('John', 'Wick', 450000, 'Senior Manager')

# accessing the Class variable (without object creation)
print('The file path = ', Employee.file)
"""
Framework :
Project Folder - Usually we have 1 project folder (or root folder) per Framework 
Packages - collection of modules (module - .py file)
Module - collection of methods/functions, variables, classes and objects
"""
