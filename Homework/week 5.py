# Week 5 HW - Joshua Greaves

numbers = [] 
while len(numbers) < 101:
    numbers.append("")

used = 0 
total = len(numbers)
turn = "A"
while total > -1:
    turnOver = False
    while turnOver == False:
        number = int(input("What number? "))
        while number < 0 or number > 100: 
            print("That number is invalid!")
            number = int(input("What number? "))
        if numbers[number] == "": 
            numbers[number] = turn 
            total -= 1 
            turnOver = True
            print(numbers)
        else: 
            print("Sorry that is already taken! Please pick another one")

    if turn == "A": turn = "B"
    elif turn == "B": turn = "C"
    else: turn = "A"
    used += 1 

    print("You have", str(len(numbers) - used), "left!") 
