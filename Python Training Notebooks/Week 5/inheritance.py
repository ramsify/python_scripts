class Employee:  # class definition

    def __init__(self, first, last, salary):
        print('Constructor invoked for Employee class')
        self.first = first
        self.last = last
        self.salary = salary
        self.fullname()
        self.email()

    def fullname(self):  # instance method to print full name
        return self.first + ' ' + self.last
        # print('Employee name = {}'.format(full_name))

    def email(self):  # instance method to print email
        email = (self.first + '.' + self.last + '@abc.com').lower()
        print('Email = {}'.format(email))


class Developer(Employee):  # single inheritance - class has additional attribute - technology
    def __init__(self, first, last, salary, technology):
        print('Invoking Developer class constructor')
        super().__init__(first, last, salary)  # invoking super class constructor
        # Employee.__init__(self, first, last, salary) - another way to invoke super class constructor
        print("The Developer's primary skill = {}\n------".format(technology))


class Manager(Employee):  # single inheritance - class has additional attribute - reportees
    def __init__(self, first, last, salary, reportees=None):
        print('Invoking Manager class constructor')
        super().__init__(first, last, salary)  # invoking super class constructor
        if reportees is None:
            self.reportees = []
        else:
            self.reportees = reportees
        self.print_reportees()

    def print_reportees(self):
        print('The reportess are:')
        for i in self.reportees:
            print(i.fullname())


dev1 = Developer('Rick', 'Grimes', 1000, 'Machine Learning')
dev2 = Developer('Joel', 'Hacker', 2000, 'Full Stack Development')

mgr1 = Manager('John', 'Wick', 10000, [dev1, dev2])


# =================================
class A:
    pass


class B:
    pass


class C(A, B):  # multiple inheritance
    pass


# ==================================
class D(C):  # multilevel inheritance
    pass
