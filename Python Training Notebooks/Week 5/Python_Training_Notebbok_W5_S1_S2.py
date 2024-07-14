"""
OOPs - Object oriented Programming
Python has 2 coding paradigms - Functional paradigm & OOPs paradigm
(For the last 4 weeks we used Python in Functional paradigm)
-----------------

In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
It aims to implement real-world entities like
    inheritance, polymorphisms, encapsulation, etc. in the programming.
The main concept of OOPs is to bind the data and the functions that work on that together as a single unit
so that no other part of the code can access this data.

OOPs - is heavily used in the frameworks
    1) binds the code and data
    2) Very structured and legible
    3) easy to maintain
    4) more inclined towards reusability

(Note: You can create frameworks in Functional paradigm as well)

OOPs Concepts in Python
=======================
Class
Objects
Polymorphism
Encapsulation
Inheritance
Data Abstraction

Python Class
============
A class is a collection of objects.
A class contains the blueprints or the prototype from which the objects are being created.
It is a logical entity that contains some attributes and methods.

Python Objects
==============
An Object is an instance of a Class.
A class is like a blueprint while an instance is a copy of the class with actual values.
Python also supports object-oriented programming that stresses objects
i.e. it mainly emphasizes functions.
Python Objects are basically an encapsulation of data variables and methods
acting on that data into a single entity.
 
Creating an object for a class is called Instantiation.
There can be n number of instances for a class.

Syntax for creating an object:
=============================
obj_name = class_name(attributes/params)

example
-------
emp1 = Employee(attributes/params)

------------------------------------------------------------
Instance variables:
===================
    Instance variables are prefixed with 'self.'
    Can be accessed only via instances
    Cannot be accessed using class/static methods

Instance methods:
================
    If a method inside a class leverages any of the instance variable then it should be an
    instance method.
    By default, the first param for instance method is 'self'.
    Decorators are not required for instance methods.

Class variables:
================
    Class variables are static. They can be accessed or updated using
       1. Class methods
       2. Instance methods
       3. Static methods
    Can be accessed using class name(via class methods/static methods/instance methods)
    Can be access using instance name (via instance methods)
    We actually don't need to instantiate a class to for using class variables.

Class methods:
==============
The classmethod() methods are bound to a class rather than an object.
Class methods can be called by both class and object.
These methods can be called with a class or with an object (instance).
A class method takes 'cls' as the first parameter.
A class method can access or modify the class state
We use the decorator '@classmethod' before the method definition

A class method receives the class as the "implicit" first argument,
just like an instance method receives the instance.

Static methods:
==============
Static methods, much like class methods, are methods that are bound to a class rather than its object.

They do not require a class instance creation.
So, they are not dependent on the state of the object.

Differences between a static method and a class method:
============================================================
Static method knows nothing about the class and just deals with the parameters.
Class method works with the class since its parameter is always the class itself.
Static methods do not have any "implicit" first argument unlike classes or instances.
They are as same as regular functions in python except for that they are defined inside a class.
We use the decorator '@staticmethod' before the method definition
Static methods can have their own local variables which cannot be accessed by class/instances.
"""


class Employee:  # class definition
    raise_percent = 25  # class variable

    # __init__ method is a constructor that gets invoked implicitly during object creation
    # for instance methods - by default self is the first param (similar to that of 'this' in java)
    def __init__(self, first, last, salary, designation):
        print('Constructor invoked')
        self.first = first
        self.last = last
        self.salary = salary
        self.designation = designation
        self.fullname()
        self.email()
        self.basic_calc()
        self.revised_sal_calc()

    def fullname(self):  # instance method to print full name
        print('Employee name = {} {}'.format(self.first, self.last))

    def email(self):  # instance method to print email
        email = (self.first + '.' + self.last + '@abc.com').lower()
        print('Email = {}'.format(email))

    def basic_calc(self):  # instance method to calculate the basic component
        basic = (40 * self.salary) / 100
        print('Basic component = ', basic)

    def revised_sal_calc(self):
        # instance method to calculate revised_salary based on derived raise_percentage
        actual_raise = Employee.raise_per_calc(self.designation)
        rev_salary = self.salary + (self.salary * actual_raise) / 100
        print('The Revised salary = {} \n-----------'.format(rev_salary))

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


# instantiation/object creation
emp1 = Employee('Michael', 'Schofield', 100000, 'Manager')
emp2 = Employee('John', 'Wick', 100000, 'Architect')
emp3 = Employee('John', 'Wick', 250000, 'Senior Manager')

# accessing the Class variable (without object creation)
print('Accessing the class variable "raise_percent". '
      'Value = ', Employee.raise_percent)
