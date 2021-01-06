#program for calculating electricity bill in Python
units=int(input("please enter the number of units you consumed in a month"))
if(units<=50):
    bill_amount=units*3
    
elif(units<=100):
    bill_amount=units*6
 
elif(units<=150):
    bill_amount=units*9
    
elif(units<=200):
    bill_amount=units*12
    
elif units<=201:
    bill_amount=units*15
else:
    print("enter the valid amount")

print("units",units)
print("bill amount in dollers",bill_amount)