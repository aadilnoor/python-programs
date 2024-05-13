class Parent:
    def fun(self,call):
        print("this function is in parent")

class Child(Parent):
    def disp(self):
        super().fun(10)
        print("this funcrion is in Child")
        
c=Child()
c.disp()          