import random, re, time

def scoreCalc(card, player): #The card to score & whether it is the player or not
	if re.match("[0-9]", card[1]): #If the card is a number  
		if (card[1] == "1"): # If the card is 10 (there's no card 1, so it has to be 10)
			score = 10 # Set the score to 10 (pip value) 
		else: # If the score is anything but 10 
			score = int(card[1]) # Set the score to the pip value on the card 
		
	elif re.match("[JQK]", card[1]): # If the card is a face card 
		score = 10 # Set the score to 10 
	
	elif card[1] == "A": #If the card is an ace - ask what value they'd like 
		if (player): 
			print("\n\nYou have drawn an Ace, would you like this to equal 11 or 1?")
			while True: # Continue until the value is correct 
				try: # Try this, if either it is not an int or not 1/11 it will retry 
					UserInput = int(input("> ").strip()) # Ask for the user input 
					if UserInput == 11 or UserInput == 1: #Check whether it is 1/11
						score = UserInput
						break # Break the infinite loop 
					else: 
						raise Exception() # Else, raise an exception 
				except: # Display an error message 
					print("Sorry! That value was not accepted \nPlease enter either 1 or 11!")
					print(UserInput)
		else: # Temporary computer algorithm  
			compChoice = random.randint(0, 1) # 50/50 chance whether the computer decides to pick 1/11 with Ace
			if compChoice == 1: 
				score = 11
			else: 
				score = 1 
	else: 
		print("Error scoring" + card[1]) # If one of the above catchments have not fired - this should not occur. 

	return score


def PlayerTurn(): # When it is the player's go 
	global playerScore # Access playerscore - Not sure why both of these have to be here 
	global standOff # Access standOff state

	print("\n" * 49)

	print("Computer Hand: (?)") # Output the hands 
	print("- Hidden Card")
	outputHand(computerHand, 1)
	print("")
	
	print("Your Hand: (" + str(playerScore) + ")")
	outputHand(playerHand, 0)
	print("")
	print("It is your turn!\nWould you like to 'hit' or 'stand'?") 
	while True:
		try: 
			UserInput = input("> ").lower().strip() # Ask what they'd like to do 
			if UserInput == "hit" or UserInput == "twist": # If they would like to twist 
				standOff = 0 # Stand off reset 
				card = deck.pop(0) # Remove card from deck 
				playerHand.append(card)# Add card to hand 
				playerScore = playerScore + scoreCalc(card, True) # add the score 

				print("\n" * 49)
				print("You have recieved the card - " + card)
				print("Your score is now " + str(playerScore))
				break 
			elif UserInput == "stand" or UserInput == "stick": # If the player decided to stand 
				standOff += 1 # Increase the standOff score 

				print("\n" * 49)
				print("You did not pick up a card.")
				print("Your score remains at " + str(playerScore))
				break
			else: 
				raise Exception() # If they failed to put in a valid response 		
		except: 
			print("Sorry, that is not an option!\nPlease enter either 'stand' or 'hit'")

	time.sleep(2) # Delay the code by 2 seconds 
	switchPlayer("computer")


def ComputerTurn(): # Computer's hand - probability based 
	global computerScore
	global playerHand
	global standOff
	
	print("\n" * 49) # Print the hands 
	print("Computer Hand: (?)")
	print("- Hidden Card") 
	outputHand(computerHand, 1)
	print("")

	print("Your Hand: (" + str(playerScore) + ")")
	outputHand(playerHand, 0)
	print("")
	print("The computer is deciding...") # Output to "show" the decision making

	time.sleep(1) # Delay the script, so it doesn't got a lightning speed 
	triggered = False # Check whether they have decided to play or stand 
	chance = random.randint(0, 100) # Random chance generator 

	if computerScore > 17:
		if chance < 10: # Over 17 = 10% chance 
			triggered = True

	if computerScore < 18 & computerScore > 14: 
		if chance < 25: # Under 17 but over 14 = 25% chance 
			triggered = True

	if computerScore < 15 & computerScore > 11: 
		if chance < 50: # Under 15 but over 11 = 50% chance 
			triggered = True
			
	if computerScore < 12: # Always play if they're under 12. 
		triggered = True

	
	if triggered:
			card = deck.pop(0) #If the computer decides to play, get a card
			computerHand.append(card) # Add card to hand 
			computerScore = computerScore + scoreCalc(card, False) #Add to score
			print("\n\nThe computer has decided to pick up a card!")
	else: 
		standOff += 1 # If the computer is standing - add to count. 
		print("\n\nThe computer has decided to stand!")

	time.sleep(2) # Delay so player can view decision
	switchPlayer("player") # Switch player 

def switchPlayer(person): # Winning / losing check when switching player 
	if person == "player": # If they are switching to a computer (the player has just had their go) 
		if (len(computerHand)) == 5: # If the computer has 5 cards, no need to check computer 
			winner("computer", "Five cards in hand!")
		elif computerScore > 21: # If the computer's score is over 21
			winner("player", "Computer scored over 21!") # Player has won 
		elif standOff == 2: # If both players have decided to stand 
			if computerScore > playerScore: # Check who has the highest 
				winner("computer", "Stand off - Computer has the highest!")
			else: 
				winner("player", "Stand off - Player has the highest!")
		elif computerScore == 21: # If the computer has managed to blackjack  
			winner("computer", "Computer got a score of 21!")
		else: #Player's go 
			PlayerTurn()

	else: # See above comments for what each catchment does 
		if (len(playerHand)) == 5: 
			winner("player", "Five cards in hand!")
		elif playerScore > 21: 
			winner("computer", "Player scored over 21!")
		elif standOff == 2:
			if computerScore > playerScore: 
				winner("computer", "Stand off - Computer has the highest!")
			else: 
				winner("player", "Stand off - Player has the highest!")
		elif playerScore == 21: 
			winner("player", "Player got a score of 21!")
		else: #Computer's go 
			ComputerTurn()

def winner(player, reason): # Display the end game/winner/loser screen 
	print("\n" * 49)
	if player == "player": #If the player has won
		print("""
░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝""")
	else: #If the player has lost 
		print("""\n\n\n\n\n\n\n\n\n
██╗░░░░░░█████╗░░██████╗███████╗██████╗░
██║░░░░░██╔══██╗██╔════╝██╔════╝██╔══██╗
██║░░░░░██║░░██║╚█████╗░█████╗░░██████╔╝
██║░░░░░██║░░██║░╚═══██╗██╔══╝░░██╔══██╗
███████╗╚█████╔╝██████╔╝███████╗██║░░██║
╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")

	print("")
	print("Winner - " + str(player).capitalize()) #Show the winner 
	print("Reason - " + reason) #Show why they have won 

	print("\nYour Hand: (" + str(playerScore) + ")")
	outputHand(playerHand, 0) #Output all of the player's hand 
	print("")

	print("Computer's Hand: (" + str(computerScore) + ")")
	outputHand(computerHand, 0) #Output all of the computer's hand 
	input()

def outputHand(hand, start): #Output the hand; hand = the hand they'd like to output; index = the index point they'd like to start outputting (used to hide the first card in the opponent's hand)
	x = start
	while x < len(hand): # This section makes the card "user friendly" so they are not displayed C5, that'd be converted to Five of Clubs (unicode is used, but this is not supported in Python command line)
		string = "- "
		if hand[x][1] == "A":
			string += "Ace of "
		elif hand[x][1] == "2":
			string += "Two of "
		elif hand[x][1] == "3":
			string += "Three of "
		elif hand[x][1] == "4":
			string += "Four of "
		elif hand[x][1] == "5":
			string += "Five of "
		elif hand[x][1] == "6":
			string += "Six of "
		elif hand[x][1] == "7":
			string += "Seven of "
		elif hand[x][1] == "8":
			string += "Eight of "
		elif hand[x][1] == "9":
			string += "Nine of "
		elif hand[x][1] == "10":
			string += "Ten of "
		elif hand[x][1] == "J":
			string += "Jack of "
		elif hand[x][1] == "Q":
			string += "Queen of "
		elif hand[x][1] == "K":
			string += "King of "
		
		if hand[x][0] == "C": 
			string += "♣"
		elif hand[x][0] == "S": 
			string += "♠"
		elif hand[x][0] == "H": 
			string += "♥"
		elif hand[x][0] == "D": 
			string += "♦"
		
		x += 1
		print(string)
		
		

	


deck = ["CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK", "SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", "HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK"]
random.shuffle(deck) # Shuffle the deck

standOff = 0 # Default staffOff to 0 
playerHand = [deck.pop(0), deck.pop(1)] # Assign the cards
computerHand = [deck.pop(2), deck.pop(3)]

print("\n" * 49)
print("Generating your hand...") 
outputHand(playerHand, 0) # If they get dealt an Ace on the first go they can see what other cards they have 

playerScore = scoreCalc(playerHand[0], True) # Done separately just in case they get an ace, more user friendly 
playerScore += scoreCalc(playerHand[1], True)

computerScore = scoreCalc(computerHand[0], False) + scoreCalc(computerHand[1], False)

print("\n" * 49)
input("""Welcome to... 
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

Press enter to continue...""") # Welcome screen 
print("\n" * 49)
PlayerTurn() # Start the game
