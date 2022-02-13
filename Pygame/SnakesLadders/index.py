import time 
import pygame 
import random 
import os
import math 

# Improvements 
# - Smooth movement of tokens 
# - Display the die roll

from pygame.constants import QUIT 

pygame.init() 
pygame.font.init()

width = 1000
height = 855
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # Where your .py file is located
assets_path = os.path.join(current_path, 'assets') # The resource folder path
font = pygame.font.SysFont('Comic Sans MS', 30)

class ladder: 
    def __init__(self):
        pass

class snakes: 
    def __init__(self):
        pass

def addSnakes(number, board): 
	numberAdded = 0 
	while numberAdded < number: 
		place = random.randint(0, len(board))
		length = -random.randint(3, 15)
		if (place+length) > 0 and board[place] == 0 and board[place+length] == 0:
			board[place] = length
			numberAdded += 1

def addLadders(number, board): 
	numberAdded = 0 
	while numberAdded < number: 
		place = random.randint(0, len(board))
		length = random.randint(3, 10)
		if (place+length) < 100 and board[place] == 0 and board[place+length] == 0:
			board[place] = length
			numberAdded += 1

def positionCentre(pos):
	if (pos <= 9) or (pos >= 20 and pos <= 29) or (pos >= 40 and pos <= 49) or (pos >= 60 and pos <= 69) or (pos >= 80 and pos <= 89): row = 1 
	else: row = 2

	if row == 1: x = 128 + ((pos % 10) - 1) * 85
	else: x = 727 - ((pos % 10) - 1) * 85

	if pos < 10: col = 0 
	else: col = int(str(pos)[0]) 
	y = 855 - (128 + (col-1) * 85)
	
	
	return (x, y)

def takeTurn(board, players, player): # Returns the next player to take a turn
	roll = random.randint(1, 6)
	newPlace = players[player] + roll + board[players[player] + roll]
	players[player] = newPlace

	return switchPlayer(player, players)

def switchPlayer(player, players): 
	player += 1
	if player >= len(players): player = 0
	return player 





def gameLoop(): 
	gameExit = False
	board = [0 for i in range(100)]
	players = [0 for i in range(2)]
	playerColours = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(len(players))]

	player = 0
	addSnakes(5, board)
	addLadders(5, board)

	while not gameExit:
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT: 
				gameExit = True
			if e.type == pygame.KEYDOWN: 
				if e.key == pygame.K_SPACE: 
					player = takeTurn(board, players, player)
	
		screen.fill((255, 255, 255))
		
		# Draw the grid
		pygame.draw.rect(screen,(0,0,0),(0,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(85,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(170,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(255,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(340,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(425,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(510,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(595,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(680,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(765,0,5,855))
		pygame.draw.rect(screen,(0,0,0),(850,0,5,855))

		pygame.draw.rect(screen,(0,0,0),(0,0,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,85,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,170,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,255,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,340,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,425,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,510,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,595,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,680,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,765,855,5))
		pygame.draw.rect(screen,(0,0,0),(0,850,855,5))

		place = 0
		while place < len(board):
			if board[place] != 0:
				pos1 = positionCentre(place)
				pos2 = positionCentre(place+board[place])
				if board[place] < 0: pygame.draw.line(screen, (255,0,0), pos1, pos2, 5)
				else: pygame.draw.line(screen, (0,255,0), pos1, pos2, 5)
			place += 1

		plyr = 0 
		while plyr < len(players):
			# print("player", plyr, players[plyr])
			# print(positionCentre(players[plyr]))
			pygame.draw.circle(screen, playerColours[plyr], positionCentre(players[plyr]), 5)
			plyr += 1

		pygame.display.update()
		clock.tick(100)


gameLoop()
pygame.quit()
quit()
