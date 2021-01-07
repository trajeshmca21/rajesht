# function to find maximum position in list 
def minimum(a, n): 

	
	
	# function to find the position of maximum 
	minpos = a.index(min(a)) 
	
	# printing the position 
	print("The maximum is at position", minpos + 1)
	
	
	

a = [3, 4, 1, 3, 4, 5,9,6,1,5] 
b=tuple(a)
minimum(a, len(b)) 
