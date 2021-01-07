def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "python training"  
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s))
print("length of string",len(s))