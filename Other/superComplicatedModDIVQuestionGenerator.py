from random import *
# From shared drive

def generateMODQuestion(difficulty):
	num1 = randint(5*difficulty, 10*difficulty)
	num2 = randint(2, num1 // 2)
	print("what is", num1, "MOD", num2,"?")
	answer = num1 % num2
	return answer

def generateDIVQuestion(difficulty):
	num1 = randint(5*difficulty, 10*difficulty)
	num2 = randint(2, num1 // 2)
	print("what is", num1, "DIV", num2,"?")
	answer = num1 // num2
	return answer

difficulty = -1
while difficulty <2 or difficulty > 10:
	difficulty = int(input("Enter a dificulty between 2 and 10 -"))

again = "y"
score = 0
count = 0	
while again == "y":
	if count % 2 == 0:
		answer = generateMODQuestion(difficulty)
	else:
		answer = generateDIVQuestion(difficulty)
	userAnswer = int(input("What is the answer?"))
	if answer == userAnswer:
		print("correct!")
		score+=1
	else:
		print("sorry, the answer is", answer)
	
	count+=1
	again = input("Do you want to go again?(y/n)")

print("you got", score, "out of", count)

print("which is", (score/count) * 100, "%")
	
