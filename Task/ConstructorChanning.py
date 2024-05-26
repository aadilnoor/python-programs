class Vehicle:
    def __init__(self,engine):
        print("Inside the Vehicle constructor")
        self.engine=engine
        print(engine)

class Car(Vehicle):
    def __init__(self, engine,speed):
        super().__init__(engine)
        print("Inside the car constructor")
        self.speed=speed
        
obj = Car("Turbo","400kmh")