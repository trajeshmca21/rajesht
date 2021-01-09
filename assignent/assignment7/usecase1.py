
class Car:
    def __init__(self,model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
    def start(self):
        print ("Engine started")
    def move(self):
        print("to move a car")

    def engine(self):
        print ("Engine switched off")
    def car_info(self):
        print("car model is:   ",self.model)
        print("car brand:      ",self.brand)
        print("car color:      ",self.color)
class Bmw(Car):
    def __init__(self,model,brand,color):
        super().__init__(model,brand,color)
    def autoPilot(self):
        print ("autoPilot")
    def  autoGear(self):
        print(" autoGear")
    
    
    
        
d=Bmw("audi","c22as","red")
d.car_info()
d.start()
d.move()
d.engine()
d.autoGear()
d.autoPilot

