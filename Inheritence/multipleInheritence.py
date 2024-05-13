class Parent1:
    def func1(self):
        print("This function is in parent 1")

class Parent2:
    def func2(self):
        print("This function is in parent 2")

class Child(Parent1, Parent2):
    def func3(self):
        print("This function is in child")


obj = Child()
obj.func1()
obj.func2()
obj.func3()