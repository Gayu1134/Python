for i in range(5):
	for j in range(5):
		if(i==1 and j!=0):
			print(" ",end=" ")
		else:
			if(i==3 and j!=4):
				print(" ",end=" ")
			else:
				print("+",end=" ")
	print()
