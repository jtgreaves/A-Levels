import random

#Define how big the triangle should be 
print("How long should the triangle be?")
rows = int(input("> "))

#Set the triangle's first row up, randomly generating the desired length 
triangle = [[]]
while len(triangle[0]) < rows:
    triangle[0].append(random.choice(["R", "G","B"]))

#Fill in the rest of the triangle 
pos = 1
while pos < rows:
    #Add another list/row 
    triangle.append(list())
    ind = 0

    #Loop through the row, appending a new RBG based on the previous row
    while len(triangle[pos]) < rows-pos:
        temp_1 = triangle[pos-1][ind]
        temp_2 = triangle[pos-1][ind + 1]

        #Conditons
        if temp_1 == temp_2:
            triangle[pos].append(temp_1)
            # print(temp_1, temp_2, "produced", temp_1)
        elif (temp_1 == "R" or temp_2 == "R") and (temp_1 == "G" or temp_2 == "G"):
            triangle[pos].append("B")
            # print(temp_1, temp_2, "produced B")
        elif (temp_1 == "R" or temp_2 == "R") and (temp_1 == "B" or temp_2 == "B"): 
            triangle[pos].append("G")
            # print(temp_1, temp_2, "produced G")
        elif (temp_1 == "B" or temp_2 == "B") and (temp_1 == "G" or temp_2 == "G"): 
            triangle[pos].append("R")
            # print(temp_1, temp_2, "produced R")
        
        ind += 1
    pos += 1 

# Loop through and print the triangle
pos = 0
while pos < len(triangle): 
    ind = 0
    line = " " * pos
    while ind < len(triangle[pos]): 
        line += " " + str(triangle[pos][ind])
        ind += 1

    print(line)
    pos += 1
