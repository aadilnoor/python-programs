class Animal:
    def dog(self):
        print("dog is barking")


class Lion(Animal):
    def lion(self):
        print("lion is roar")    
    

class Cat(Lion):
    def cat(self):
        print("cat is sleeping")
c=Cat()
c.dog()
c.lion()
c.cat() 