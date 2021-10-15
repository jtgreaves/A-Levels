def cipherSentence(sentence):
	sentenceVariations = []
	words = sentence.split(" ")
	
	# Loops through all the words in a sentence 
	counter = 0 
	for word in words:
		sentenceVariations.append([])
		
		# Finds all cipher posibilities of the words
		i = 0 
		while i < 26: 
			sentenceVariations[counter].append(cipherWord(word, i))
			i += 1
		counter += 1
	
	leaderboard = rankWords(sentenceVariations)
	return sentenceVariations
	
	
# Ciphers a singular word
def cipherWord(word, i):
	finalWord = ""
	for x in word:
		asc = ord(x)
		asc += i
		if asc > 122:
			asc -= 26
		
		finalWord = finalWord + chr(asc)
	 
	return finalWord
	
	
def searchDictionary(word):
	if ("\n" + word + "\n") in open('british-english').read(): # Checks whether the word exists (must have its own line) 
		return True
	else:
		return False

def rankWords(sentenceVariations):
	ratings = []
	for variations in sentenceVariations:
		score = 0
		
		pos =  0 
		while pos < len(variations):
			ratings.append(0)
			if searchDictionary(variations[pos]): 
				ratings[-1] =+ 1
				print(ratings)
				print("@", sentence)				
				#print(variations[pos], searchDictionary(variations[pos]))
			
			pos += 1
		 
	return sentenceVariations
	


sentence = input("What sentence would you like to decrypt? ").lower() # handles all words as lowercase
print(cipherSentence(sentence))

