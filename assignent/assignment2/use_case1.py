

roll_no=int(input("enter the roll number:  " ))
name=input("enter name:    ")
print("Enter marks six subjects")
S1=float(input("enter the subject1"))
S2=float(input("enter the subject2"))
S3=float(input("enter the subject3"))
S4=float(input("enter the subject4"))
S5=float(input("enter the subject5"))
S6=float(input("enter the subject6"))

total = S1 + S2 + S3 + S4 + S5+S6
avg = total/6.0
print("Total marks =" , total)
print("Average marks =", avg)


if avg>=80:
    print("A grade")
elif avg<79 and avg>60:
    print("B grade")
    
elif avg<59 and avg>50:
    print("C grade")
elif avg<40 and avg>49:  
    print("D grade")
else:
    print('promoted')



