word = input("Please enter your word") 

maxCol = 80
maxRows = 20

numberOfWords = maxCol // len(word) 
offset = maxCol % len(word) 

row = 0 
col = 0 
temp = ""

while row < maxRows:
	print(temp, (word + " ") * numberOfWords, word[0:offset])
	temp = word[offset:len(word)]
	row += 1

