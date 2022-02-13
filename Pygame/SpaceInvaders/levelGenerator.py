import json 
import os

current_path = os.path.dirname(__file__)
levels_path = os.path.join(current_path, 'levels')

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

filePath =  os.path.join(levels_path, levelName + ".json")

# f = open(filePath, "x")
f = open(filePath, "w")
f.write(jsonObj)
f.close()

