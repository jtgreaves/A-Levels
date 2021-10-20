while True: 
	y = int(input("Please enter a positive number - "))
	output = ""
	while y > 0: # While a positive number
		print ("y", y) 
		digit = y % 2 # Remainder when divided by 2 
		print("digit", digit)
		y = y  // 2 # Clean division 
		print("y2", y)
		output = str(digit) + output # Concatenates digit & y 
		print(output)
	print("FINAL", output)
