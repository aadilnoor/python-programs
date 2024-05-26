class A:
    
    def __init__(self,name):
        print("Hello",name)
    
    def __init__(self,age , name ):
        self.age=age
        self.name=name
        print(age,name)
ob = A(21,"Aadil")
ob2 = A(20,"Noor")

     