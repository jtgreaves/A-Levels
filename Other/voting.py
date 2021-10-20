ACount = 0 
BCount = 0 
CCount = 0

vote = ""
while vote != "end":
	vote = input("What would you like to vote? ")
	
	if vote.lower() == "a": 
		ACount += 1 
	elif vote.lower() == "b": 
		BCount += 1
	elif vote.lower() == "c": 
		CCount += 1
print(ACount, BCount, CCount)
