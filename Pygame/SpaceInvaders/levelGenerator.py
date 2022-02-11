import json 


invaders = []
userInput = "" 
while userInput != "exit": 
	userInput = input("Exit to stop appending ")
	if userInput != "exit": invaders.append(int(userInput))

	print(invaders)
	
x = {
  "levelName": "Beginner",
  "invaders": invaders, 
  "barricades": 1
}

jsonObj = json.dumps(x)

levelName = input("What is the level's name? ")

f = open("levels/" + levelName + ".json", "w")
f.write(jsonObj)
f.close()

