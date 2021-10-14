
#userSentence = input("What would you like decrypt? ").lower()
#print(userSentence)
#
#userSentence = userSentence.split(" ")
#finalSentence = []
#
#i = 0 
#while i < len(userSentence): # Loop through the words 
#	p = 0
#	finalSentence.append([])
#	
#	while p < len(userSentence[i]): # Loop through the letters
#		print("#DEBUG P", finalSentence)
#		x = 0
#		print(p)
#		finalSentence[i].append([])
#		
#		while x < 26: # Calculate all cipher posibilities 
#			print (userSentence[i][p], x)
#			finalSentence[i][p] += chr(ord(userSentence[i][p]) + x)#THIS NEEDS TO BE SEPARATED SO YOU DO NOT OVERFLOW
#			x += 1
#	
#		p += 1
#	
#	print(userSentence[i])
#	i += 1 
#	
#print(finalSentence)
#


def cipherSentence(sentence):
	sentenceVariations = []
	words = sentence.split(" ")
	
	print(words)
	counter = 0 
	for word in words:
		sentenceVariations.append([])
		
		i = 0 
		while i < 26: 
			
		sentenceVariations[counter].append(cipherWord(word))
		counter =+ 1
		
	return sentenceVariations
	
	
def cipherWord(word):
	
	for x in word: 
		print(ord(x))
	 
	return word
	
	
def dictionaryCheck(word):
	print(dictionary)
	

sentence = input("What sentence would you like to decrypt? ").lower()
print(cipherSentence(sentence))

