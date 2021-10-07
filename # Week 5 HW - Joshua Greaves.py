# Week 5 HW - Joshua Greaves

numbers = [] 
while len(numbers) < 102: #102 as people need to be able to select number 0 & 101
    numbers.append("")

total = len(numbers)
turn = "A"
while total > -1:
    turnOver = False
    while turnOver == False:
        number = int()
        while number > -1 and number < 102: 
            number = int(input("What number? "))
        if numbers[number] == "": 
            numbers[number] = turn 
            total -= 1 
            turnOver = True
        else: 
            print("Sorry that is already taken! Please pick another one")

    if turn == "A": turn = "B"
    elif turn == "B": turn = "C"
    else: turn = "A"
