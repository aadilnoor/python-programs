class Computer:
    def __init__(self,name,price):
        
        self.__name=name
        self.__price=price

    def display(self):
        print(self.__name,self.__price)
     
c = Computer("Dell",12000)
c.display()
