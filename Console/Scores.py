from random import * 
scores = [randint(1,999) for a in range(200)]
#scores = [1, 2, 3, 50, 103, 2, 3, 1]
print(scores)

def maxScore(list): 
	pos = 0 
	currentMax = 0 
	currentMaxPos = 0 
	while pos < len(list): 
		if list[pos] > currentMax: 
			currentMax = list[pos] 
			currentMaxPos = pos
		pos += 1 

	return currentMaxPos

def topScores(list): 
	scrs = []
	while len(scrs) < 3: 
		pos = maxScore(list)
		scrs.append(list.pop(pos))
	return scrs





def minScores(list):
	pos = 0 
	currentMin = list[0]
	currentMinPos = 0
	while pos < len(list): 
		if list[pos] < currentMin: 
			currentMin = list[pos] 
			currentMinPos = pos
		pos += 1 

	return currentMinPos

def bottomScores(list): 
	scrs = []
	while len(scrs) < 3: 
		pos = minScores(list)
		scrs.append(list.pop(pos))
	return scrs

print("TOP SCORES:", topScores(scores))
print("BOTTOM SCORES:", bottomScores(scores))
