# Joshua Greaves

import random  

highScores = open("scores.txt", "r").read().split("\n")

# Have not fully tested this.
x = 1
highScore = 0
index = x 
while x < len(highScores):
	if highScore < int(highScores[x]):
		highScore = x 
		index = x 
	x += 2 
print("Highest score is", highScores[index-1], "with", highScores[index])

print("\nWelcome to brain training \nYou will be asked some questions!")
name = input("Please enter your name.. ")
nickname = input("Please enter your nickname.. ")
score = 0

print("\nOkay,", name + ". I will call you", nickname + "!")

while True: 
	try:
		maxQuestion = int(input("\nBefore we start, how many questions would you like? ")) + 1
		break
	except:
		print("\nSorry, that is not an acceptable number.")

while True:
	try: 
		difficulty = int(input("What difficulty would you like (1 - 10)? "))
		if difficulty > 10 or difficulty < 1: 
			raise Exception()
		else: 
			break;
	except: 
		print("\nSorry, that is not an acceptable difficulty.")
	
questionNumber = 1 

def cleanDivide(num1, num2): 
	if (num1 % num2) == 0: 
		return True
	else:
		return False

while questionNumber < maxQuestion:  
	num1 = random.randint(1,10) * difficulty
	num2 = random.randint(1,10) * difficulty
	questionChoice = random.randint(1, 4)
	
	if questionChoice == 1: 
		operator = "+"
		correctAnswer = num1 + num2
	elif questionChoice == 2:
		operator = "-"
		correctAnswer = num1 - num2
	elif questionChoice == 3: 
		operator = "*"
		correctAnswer = num1 * num2
	elif questionChoice == 4: 
		operator = "/"
		
		clean = False
		while clean == False:
			if cleanDivide(num1, num2) == False: 
				num1 = random.randint(1,10) * difficulty
				num2 = random.randint(1,10) * difficulty
			else:
				clean = True
				
		correctAnswer = num1/num2
			
	print("\n\nQuestion", str(questionNumber) + "\n", num1, operator, num2, "= ?")
	
	try: 
		response = int(input("What is your answer? "))
	except ValueError:
		response = int(100001) #This should not be a possible answer
			
	if response == correctAnswer:
		print("\nCorrect!")
		score += 1 
	else:
		print("\nIncorrect!") 
	print("Your score is,", str(score) + "!")
	
	questionNumber += 1

print("\n\nYour final score is", str(score))
scores = open("scores.txt", "a").write(name + "\n" + str(score) + "\n")
