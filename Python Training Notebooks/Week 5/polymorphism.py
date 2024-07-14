# polymorphism - many forms

def fun(a, b, c=0):  # method overloading
    return a + b + c


print(fun(1, 2))
print(fun(1, 2, 3))


# method overriding
class A:
    @staticmethod
    def fun():
        print('Function of class A')


class B:
    @staticmethod
    def fun():
        print('Function of class B')


A().fun()
B().fun()
