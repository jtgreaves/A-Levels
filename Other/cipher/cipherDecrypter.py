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
	
	
	topIndexes = findTop(rankWords(sentenceVariations))
		
	results = []
	for x in topIndexes:
		finalWord = "" 
		for y in sentenceVariations: 
			finalWord = finalWord + y[x] + " "
		results.append(finalWord)
		
	return results
	
	
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
	ratings = [0]*26
	x = 0
	while x < len(sentenceVariations):
				
		pos =  0 
		while pos < len(sentenceVariations[x]):
			if searchDictionary(sentenceVariations[x][pos]): 
				ratings[pos] += 1
							
			pos += 1
		x += 1
	return ratings

def findTop(leaderboard):
	bestIndexes = []
	stopSearch = False
	while len(bestIndexes) < 5 and stopSearch == False: # Loop until 5 found or stop declared
		largestPos = None
		largest = 0
		pos = 0
		
		while pos < len(leaderboard): # Loop through all the indexes to find the highest scoring 
			if leaderboard[pos] > largest: 
				largestPos = pos
				largest = leaderboard[pos]
			pos += 1
		
		if largestPos == None:
				stopSearch = True
		else:
			leaderboard[largestPos] = -1
			bestIndexes.append(largestPos)
			
	
	return(bestIndexes)
	
	 
	

sentence = input("What sentence would you like to decrypt? ").lower() # handles all words as lowercase
decrypted = cipherSentence(sentence)

pos = 0
print("Here are the most likely results:") 
while pos < len(decrypted): 
	print(str(pos + 1) + ". " + decrypted[pos])
	pos += 1
