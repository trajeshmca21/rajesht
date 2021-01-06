a=int(input("entrt the first number"))
b=int(input("entrt the second number"))
print("""
1. ADD
2. SUB
3. MUL
4. DIV
0. Exit

""")
opt=int(input("enter your option"))
if opt==1:
    print("add",a+b)
elif opt==2:
    print("sub",a-b)
elif opt==3:
    print("mul",a*b)
elif opt==4:
    print("div",a/b)
elif opt==0:
    exit
