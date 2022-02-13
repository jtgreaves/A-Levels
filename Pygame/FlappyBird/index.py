# Flappy Bird
# You are able to move the character between randomly generating pipes, gaining points as you pass them 
# You are unable to fly above the top of the screen, into the ground or into pipes 
# Pressing F1 will reveal a debug menu, showing the positioning of the generated pipes 
#
# Improvements 
# - Improving collision detection by utilising numerous player rects 
# - Improve the falling of the character by increasing velocity as the player falls (changing it from a very set path)
# - Could revamp the gameloop, to support a wider range of screens (see TicTacToe)
# - Show (and store) the highscored
# - Show the reason for the gameover (floor/pipe)

import pygame 
import random 
import os 

pygame.init() 
pygame.font.init()

width = 1200
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # Where your .py file is located
assets_path = os.path.join(current_path, 'assets') # The resource folder path
font = pygame.font.SysFont('Comic Sans MS', 30)

character = pygame.image.load(os.path.join(assets_path, 'character.png'))
bottomPipe = pygame.image.load(os.path.join(assets_path, 'smallPipe.png'))
topPipe = pygame.transform.rotate(pygame.image.load(os.path.join(assets_path, 'smallPipe.png')), 180)

class pipe: 
	def __init__(self, XBiased):
		verticalOffset = random.randint(0, height//4) + height//6 
		self.pipeX = XBiased + random.randint(400, 550)
		self.topPipeY = verticalOffset - topPipe.get_height() 
		self.bottomPipeY = verticalOffset + random.randint(100, 175)
		self.passed = False

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

	cY = height//2
	smoothFlight = 0
	pipes = pipe.generateOriginPipes()
	gameXPos = 0
	score = 0

	while not gameExit:
		screen.fill((135, 206, 235))

		#if len(pipes) < 5:
		#	pipes.append(pipe(pipes[-1].pipeX))
		
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
			
			title = font.render('Flappy Bird', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width//2, height//2)))
		elif gamePlaying and not gamePaused and not gameOver:
			player = screen.blit(character, (width//2, cY))
			
			# Render pipes 
			i = 0
			while i < len(pipes): 
				p = pipes[i] 
				# Top pipe (p.pipeX-gameXPos, p.bottomPipeY+10, 100, 1000)
				# Bottom pipe (p.pipeX-gameXPos, p.topPipeY, 100, 597)

				if player.colliderect(pygame.Rect(p.pipeX-gameXPos, p.bottomPipeY+10, 100, 1000)) or player.colliderect(pygame.Rect(p.pipeX-gameXPos, p.topPipeY, 100, 597)):
					gameOver = True 
					print("Collision with pipe")
				

				screen.blit(topPipe, (p.pipeX-gameXPos, p.topPipeY))
				screen.blit(bottomPipe, (p.pipeX-gameXPos, p.bottomPipeY))
			
				if (p.pipeX-gameXPos) < -100: 
					pipes[i] = pipe(pipes[i-1].pipeX)

				if (p.pipeX-gameXPos) < (width//2) and not p.passed:
					print("The pipe has been passed")
					score += 1
					p.passed = True 
				i += 1 


			pygame.draw.rect(screen, (0, 255, 0), (0, height-50, width, 50))
			gameXPos += 10
			
			
			title = font.render(str(score), False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width//2, 20)))
		elif gamePaused:			
			
			title = font.render('Currently Paused', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width//2, height//2)))
		elif gameOver: 
			
			title = font.render('Game Over!', False, (0, 255, 0))
			screen.blit(title, title.get_rect(center=(width//2, height//2)))

		if debugMode: 
			
			title = font.render(("PlayerY " + str(cY) + " | GameXPos " + str(gameXPos)), False, (255, 0, 0))
			screen.blit(title, (100, 100))

			x = 0 
			while x < len(pipes): 
				
				title = font.render((str(x) + ": " + str(pipes[x].pipeX) + " | " + str(pipes[x].topPipeY) + " | " + str(pipes[x].bottomPipeY)), False, (255, 0, 0))
				screen.blit(title, (100, 50*(x+1)+100))
				x+=1
		pygame.display.update()
		clock.tick(30)

gameLoop()
pygame.quit()
quit()
