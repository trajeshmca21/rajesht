
class Tv:
    def __init__(self,model, brand):
        self.model = model
        self.brand = brand
        
    def features(self):
        print ("these are the features of tv")
    def oldtv_info(self):
        print("car model is:   ",self.model)
        print("car brand:      ",self.brand)

    
class SmartTv(Tv):
    def __init__(self,model,brand, screenSize, price,resolution):
        super().__init__(model,brand)
        self.screenSize=screenSize
        self.price=price
        self.resolution=resolution
    def  newFeatures(self):
        print ("the new  features are size price and resolution")
   
    
    
    def tv_info(self):
       
        print("car color:     ",self.screenSize)
        print("car color:     ",self.price)
        print("car color:     ",self.resolution)
d=SmartTv("lg","lg123","150X1500","15000","hd")
d.features()
d.oldtv_info()
d.newFeatures()
d.tv_info()