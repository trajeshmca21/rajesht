# function to find maximum position in list 
def minimum(a, n): 

	
	
	# function to find the position of maximum 
	maxpos = a.index(max(a)) 
	
	# printing the position 
	print("The maximum is at position", maxpos + 1)
	
	
	

a = [3, 4, 1, 3, 4, 5,9,6,1,5] 
minimum(a, len(a)) 
