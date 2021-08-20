# https://realpython.com/instance-class-and-static-methods-demystified/

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()

print("Accessing the instance method called method")
print(obj.method())

print("Accessing the class method called classmethod")
print(obj.classmethod())

print("Accessing the static method called staticmethod")
print(obj.staticmethod())

class Test:
    @staticmethod
    def method1():
        print("You are running Method 1")

    @staticmethod
    def method2():
        print("You are running Method 2")

    @staticmethod
    def method3():
        print("You are running Method 3, but also calling Method 2")
        Test.method2()

Test.method3()