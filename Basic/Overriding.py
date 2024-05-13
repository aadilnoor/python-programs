class Parent:

    def my_method(self):
        print("Calling parent method")

class Child(Parent):

    def my_method(self):
        super().my_method()
        print("Calling child method")


child = Child()
child.my_method()
