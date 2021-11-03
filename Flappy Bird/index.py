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

character = pygame.image.load(os.path.join('Flappy Bird/assets/character.png'))
bottomPipe = pygame.image.load(os.path.join('Flappy Bird/assets/smallPipe.png'))
topPipe = pygame.transform.rotate(pygame.image.load(os.path.join('Flappy Bird/assets/smallPipe.png')), 180)

class pipe: 
	def __init__(self, XBiased):
		verticalOffset = random.randint(0, height//4) + height//6
		self.pipeX = XBiased + random.randint(400, 550)
		self.topPipeY = verticalOffset - topPipe.get_height() 
		self.bottomPipeY = verticalOffset + 150

	def generateOriginPipes(): 
		pipes = []
		lastX = width

		while len(pipes) < 5:
			lastX = lastX + random.randint(450, 600)
			pipes.append(pipe(lastX))

		return pipes
	
def gameLoop(): 
	gameExit = False
	gamePlaying = False
	gamePaused = False	
	gameOver = False 
	
	debugMode = False

	cY = height/2
	smoothFlight = 0
	pipes = pipe.generateOriginPipes()
	gameXPos = 0

	while not gameExit:
		screen.fill((135, 206, 235))

		if len(pipes) < 5:
			pipes.append(pipe(pipes[-1].pipeX))
		
		# Handle smooth flight
		if gamePlaying and not gamePaused and not gameOver: 
			if smoothFlight < 0:
				cY += 5 # Defines the character height
				smoothFlight += 1
				if smoothFlight > 0: smoothFlight = 0  
			elif smoothFlight > 0 and cY > 0: # To go up 
				cY += -8
				smoothFlight -= 1
				if smoothFlight < 0: smoothFlight = 0  
			else: # Falling
				smoothFlight = -10

			if cY > height-85:
				gameOver = True 
				print("Collision with the ground!")

		# Handling inputs 
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT:
				gameExit = True
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_F1: 
					if not debugMode: debugMode = True
					else: debugMode = False
					print("Debug mode toggled")
				elif not gamePlaying and not gamePaused: # Start menu 
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
					elif e.key == pygame.K_END: 
						pygame.event.post(pygame.event.Event(pygame.QUIT))
				
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
			screen.blit(character, (width/2, cY))

			i = 0
			while i < len(pipes): 
				p = pipes[i] 
				screen.blit(topPipe, (p.pipeX-gameXPos, p.topPipeY))
				screen.blit(bottomPipe, (p.pipeX-gameXPos, p.bottomPipeY))
				
				if (p.pipeX-gameXPos) < -100: 
					pipes[i] = pipe(pipes[i-1].pipeX)

				i += 1 


			pygame.draw.rect(screen, (0, 255, 0), (0, height-50, width, 50))
			gameXPos += 10

		elif gamePaused:			
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render('Currently Paused', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width/2, height/2)))
		elif gameOver: 
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render('Game Over!', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width/2, height/2)))

		if debugMode: 
			font = pygame.font.SysFont('Comic Sans MS', 30)
			title = font.render(("PlayerY " + str(cY) + " | GameXPos " + str(gameXPos)), False, (255, 0, 0))
			screen.blit(title, (100, 100))

			x = 0 
			while x < len(pipes): 
				font = pygame.font.SysFont('Comic Sans MS', 30)
				title = font.render((str(x) + ": " + str(pipes[x].pipeX) + " | " + str(pipes[x].topPipeY) + " | " + str(pipes[x].bottomPipeY)), False, (255, 0, 0))
				screen.blit(title, (100, 50*(x+1)+100))
				x+=1
		pygame.display.update()
		clock.tick(30)

gameLoop()
pygame.quit()
quit()