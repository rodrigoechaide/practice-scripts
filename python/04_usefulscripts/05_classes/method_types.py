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