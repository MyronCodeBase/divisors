def divisor():
	num = int(input("Enter a number "))
	numRange = range(1, num)
	for i in numRange:
		if num % i == 0:
			print(i) 
divisor()