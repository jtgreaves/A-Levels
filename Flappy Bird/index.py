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
	gameOver = False 

	cY = height/2
	smoothFlight = 0

	while not gameExit:
		screen.fill((135, 206, 235))

		if gamePlaying and not gamePaused and not gameOver: 
			if smoothFlight < 0:
				cY += 5 # Defines the character height
				smoothFlight += 1
				if smoothFlight > 0: smoothFlight = 0  
			elif smoothFlight > 0: # To go up 
				cY += -8
				smoothFlight -= 1
				if smoothFlight < 0: smoothFlight = 0  
			else: # Falling
				smoothFlight = -10

			print(cY)
			if cY > height+50:
				gameOver = True 
				print("Collision with the ground!")

		# Handling inputs 
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT:
				gameExit = True 
			if e.type == pygame.KEYDOWN:
				if not gamePlaying and not gamePaused: # Start menu 
					if e.key == pygame.K_SPACE:
						gamePlaying = True
					elif e.key == pygame.K_ESCAPE: 
						pygame.event.post(pygame.event.Event(pygame.QUIT))

				elif gamePlaying and not gamePaused and not gameOver: # During the game 
					if e.key == pygame.K_ESCAPE: 
						gamePaused = True
					elif e.key == pygame.K_SPACE:
						smoothFlight = 10

				elif gamePaused: # Game Paused 
					if e.key == pygame.K_ESCAPE: 
						gamePaused = False
				
				elif gameOver: # Game Over 
					if e.key == pygame.K_SPACE: 
						gameOver = False
						gameExit = True
						gameLoop()

		# Handling drawings 
		if not gamePlaying and not gamePaused:
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render('Flappy Bird', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width/2, height/2)))
		elif gamePlaying and not gamePaused and not gameOver:
			print(cY)
			screen.blit(character, (width/2, cY))
			pygame.draw.rect(screen, (0, 255, 0), (0, height-50, width, 50))
		elif gamePaused:			
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render('Currently Paused', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width/2, height/2)))
		elif gameOver: 
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render('Game Over!', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width/2, height/2)))

		pygame.display.update()
		clock.tick(30)

gameLoop()
pygame.quit()
quit()