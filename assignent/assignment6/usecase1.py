
file = open("file.txt","r") 
Counter = 0
char=0
word=0

# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 


for i in CoList: 
	if i: 
		Counter += 1
words=i.split()
word+=len(words)
char+=len(i)
		
print("This is the number of lines in the file") 
print("lines      ",Counter) 

print("words       ",word)
print("characters   ",char)
