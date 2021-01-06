print('Enter correct username and password combo to continue')

username=input("enter username")
password=input("enter the password")

count = 0 
count += 1 


while username == username and password == password: 


    if count == 3: 
        print("\nThree Username and Password Attempts used. Goodbye") 
        break 


    elif username == 'focusit' and password == 'adisir': 
        print("Welcome! ") 
        break 
    elif username != 'focusit' and password != 'adisir': 
        print("Your Username and Password is wrong!") 
        username = input("\n\nUsername: ")
        password = input("Password: ")
        count += 1 
        continue 

    elif username == 'focusit' and password != 'adisir': 
        print("Your Password is wrong!")
        username = input("\n\nUsername: ")
        password = input("Password: ") 
        count += 1 
        continue

    elif username != 'focusit' and password == 'adisir': 
        print("Your Username is wrong!") 
        username = input("\n\nUsername: ")
        password = input("Password: ") 
        count += 1 
        continue
    
