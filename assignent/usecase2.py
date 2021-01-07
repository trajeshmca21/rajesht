
choice=0



while choice!=3:
    
    print("""My To Do App
        ============
        1. Add Task
        2. View All Tasks
        0. Exit
        """ )
    choice=int(input("enter your choice:    "))
    f=open("file1.txt",'w')
    if choice==1:
        f=open("file1.txt",'a')
        n=input("enter task name")
        f.write(n)
        print("task added")
        
        
    
        
    elif choice==2:
        f=open("file1.txt","r")
        a=f.readlines()
        for i in a:
            print("task name is\n\n",i)
        f.close

    elif choice==0:

        print("byee")
        break
    else:
        print('valid data')
        f.close