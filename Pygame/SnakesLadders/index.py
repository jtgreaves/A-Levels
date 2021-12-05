import time 
import pygame 
import random 
import os
import math 

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

def positionCentre(pos): 
	if (pos <= 9) or (pos >= 20 and pos <= 29) or (pos >= 40 and pos <= 49) or (pos >= 60 and pos <= 69) or (pos >= 80 or pos <= 80): row = 1 
	else: row = 2

	if row == 1: x = 128 + ((pos % 10) -1) * 85
	else: x = 855 - ((pos % 10) -1) * 85

	if pos < 10: col = 0 
	else: col = int(str(pos)[0]) 
	y = 855 - (128 + (col-1) * 85)
	
	
	return (x, y)
 



def gameLoop(): 
	gameExit = False
	grid = [0 for i in range(100)]

	snakes = [[85, 20]]

	while not gameExit:
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT: 
				exitGame = True 

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


		for snake in snakes:
			pos1 = positionCentre(snake[0])
			pos2 = positionCentre(snake[1])

			print(pos1, pos2)
			
			
			pygame.draw.line(screen, (0,0,0), pos1, pos2, 5)


		pygame.display.update()
		clock.tick(100)


gameLoop()
pygame.quit()
quit()
