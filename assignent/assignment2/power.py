amt = int(input("Enter Sale purchase Amount: "))


if(amt>100):
    if amt<=1000:
       disc = amt*0.0
    elif amt<=1001:
        disc=amt*0.1
    elif amt<=2001:
        disc=0.2 * amt
    else:
         disc=0.25 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")
    