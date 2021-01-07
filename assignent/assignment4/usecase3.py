a='oM sai rAm'
print(a.title())
print(a.lower())
print(a.capitalize())
# usecase4
test_str = "PyThoN"
    
print("The original string is : " + str(test_str)) 
  

res = [char for char in test_str if char.isupper()] 
  

a=list(res) 
for i in a:
    print("The uppercase characters in string are : " + i)
