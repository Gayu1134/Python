number = int(input("Enter the number : "))
i = 2
prime = False
while i<number:
	if(number%i==0):
		print("Not prime")
		prime = False
		break
	else:
		prime = True
		i+=1
if(prime):
	print("Prime")
