

from datetime import datetime

a=dict()
choice=0




while choice!=2:
    
    print("""My To Do App
        ============
        1. Add Task
        2. View All Tasks
        0. Exit
        """ )
    choice=int(input("enter your choice:    "))
    if choice==1:
        k=input("enter data:    ")
        v= input('Enter a date')
        a.update({k:v})
        print("task added")
        
    elif choice==2:
       # print(a.items())
        for k,v in a.items():
            print("task name......",k,"date....... ",v)
        
    elif choice==0:
        break
    else:
        print('valid data')