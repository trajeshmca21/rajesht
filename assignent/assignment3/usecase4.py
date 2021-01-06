a=[]
choice=0
while choice!=3:
    
    print("""My To Do App
        ============
        1. Add Task
        2. View All Tasks
        0. Exit
        """ )
    choice=int(input("enter your choice:    "))
    if choice==1:
        n=int(input("enter data:    "))
        a.append(n)
        print("task added")
    elif choice==2:
        print("your data is:    ",a)
    elif choice==0:
        break
    else:
        print('valid data')