class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

