class Animal:
    
    def eat(self):
        print("Animal is eating")
        
class Lion(Animal):
    def roar(self):
        print("Lion is roar")    
        
class Dog(Animal):
    def bark(self):
        print("dog is Barking")

obj1=Lion()
obj1.eat()
obj1.roar()
        
obj2=Dog()
obj2.eat()
obj2.bark()              