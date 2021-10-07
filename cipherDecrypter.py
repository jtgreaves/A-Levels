userSentence = input("What would you like decrypt? ").lower()
print(userSentence)

userSentence = userSentence.split(" ")
finalSentence = []

i = 0 
while i < len(userSentence): # Loop through the words 
	p = 0
	finalSentence.append([])
	
	while p < len(userSentence[i]): # Loop through the letters
		print("#DEBUG P", finalSentence)
		x = 0
		print(p)
		finalSentence[i].append([])
		
		while x < 26: # Calculate all cipher posibilities 
			print (userSentence[i][p], x)
			finalSentence[i][p] += chr(ord(userSentence[i][p]) + x)#THIS NEEDS TO BE SEPARATED SO YOU DO NOT OVERFLOW
			x += 1
	
		p += 1
	
	print(userSentence[i])
	i += 1 
	
print(finalSentence)
