class Memory:


    def __init__(self,internal, secondary, ram):


        self.internal=internal
        self.secondary=secondary
        self.ram=ram
    def getinfo(self):
        
        print("INTERNAL :{} \n secondary :{} \n and ram :{}\n".format(self.internal,self.secondary,self.ram))
class Properties:
    def __init__(self, model, brand, price, memory):

        self.model=model
        self.brand=brand
        self.price=price
        self.memory=memory
    def mobile_info(self):
        print("model Name:",self.model)
        print("brand     :",self.brand)
        print("price     :",self.price ,end='\n')
        self.memory.getinfo()
m=Memory("62 gb","128gb","6gb")
p=Properties("samsung","m31",18000,m)
p.mobile_info()