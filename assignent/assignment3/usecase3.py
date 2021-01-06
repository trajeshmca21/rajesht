
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
sub6=int(input("Enter marks of the sixth subject: "))

list=[sub1,sub2,sub3,sub4,sub5,sub6]
Sum=sum(list)
avg=a/len(list)
for i in list:
    print(i)
print("sum of list is",Sum)
print("average of list is",avg)