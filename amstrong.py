#Amstrong number
number = int(input("Enter the number : "))
n1 = number
len = 0
rem = 0
sum = 1
temp = 0
while(n1!=0):
	len+=1
	n1=n1//10
n2 = number
while(n2!=0):
	rem = n2 % 10
	for i in range(len):
		sum *= rem
	temp += sum
	sum = 1
	n2 = n2 // 10
if (number == temp):
	print("yes")
else:
	print("No") 
