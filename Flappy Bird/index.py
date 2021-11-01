import time 
import pygame 
import random 
import os 

pygame.init() 
pygame.font.init()

width = 1200
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#character = pygame.transform.smoothscale(pygame.image.load(os.path.join('Flappy Bird/assets/character.png')), (80, 65))
character = pygame.image.load(os.path.join('Flappy Bird/assets/character.png'))

def gameLoop(): 
	gameExit = False
	gamePlaying = False
	gamePaused = False

	while not gameExit:
		screen.fill((135, 206, 235))
		
		# Handling inputs 
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT:
				gameExit = True 
			if e.type == pygame.KEYDOWN:
				if not gamePlaying and not gamePaused: 
					if e.key == pygame.K_SPACE:
						gamePlaying = True

				elif gamePlaying and not gamePaused: 
					if e.key == pygame.K_ESCAPE: 
						gamePaused = True
					elif e.key == pygame.K_SPACE:
						pass

				elif gamePaused:
					if e.key == pygame.K_ESCAPE: 
						gamePaused = False

		# Handling drawings 
		if not gamePlaying and not gamePaused:
			print("START MENU")
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render('Flappy Bird', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width/2, height/2)))
		else:
			screen.blit(character, (width/2, height/2))
			pygame.draw.rect(screen, (0, 255, 0), (0, height-50, width, 50))


		pygame.display.update()
		clock.tick(30)

gameLoop()
pygame.quit()
quit()