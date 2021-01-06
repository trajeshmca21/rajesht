a = input("Enter any statement : ")#we have to enter string
vowels =['a','e','i','o','u']#these are given vowels



list1=[]# it is a empty list
for x in a:
    if (x in vowels and x not in list1):
        list1.append(x)
        #end of the loop
print("Vowels present in given statement : ",list1)
print("the number of vowels in statement:   ",len(list1))