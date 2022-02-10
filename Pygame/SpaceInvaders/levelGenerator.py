import json 

x = {
  "levelName": "Beginner",
  "invaders": [1, 0, 1, 0, 1, 0, 1], 
  "barricades": 5
}

jsonObj = json.dumps(x)

levelName = input("What is the level's name? ")

f = open("levels/" + levelName + ".json", "w")
f.write(jsonObj)
f.close()

