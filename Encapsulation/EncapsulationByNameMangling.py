class Laptop:
    def __init__(self,name,price,generation):
        
        self.__name=name
        self.__price=price
        self.__generation=generation
        

    # def display(self):
    #     print(self.__name,self.__price,self.__generation)

c = Laptop("Dell",12000,"i5")

print(c._Laptop__name)
print(c._Laptop__price)
print(c._Laptop__generation)
