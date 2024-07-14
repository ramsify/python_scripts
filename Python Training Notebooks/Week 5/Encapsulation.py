"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly
and can prevent the accidental modification of data.

"""
# public, protected and private variables
"""
-public variable : can be used anywhere (within class, sub class or outside)
-protected variable
  --protected variable  prefixed with ._
  --protected variable can be used within the parent and child/derived class
  -- not recommended to use outside the class
-private variable is prefixed with .__
  -- can be used only within a class
  -- can't be inherited or used by sub/child class
"""


class A:
    def __init__(self):
        self.x = 1
        self._y = 3
        self.__z = 4


class B(A):
    def __init__(self):
        super().__init__()
        print("The value of x = ", self.x)
        print("The value of y = ", self._y)
        print("The value of z = ", self.__z)


B()
