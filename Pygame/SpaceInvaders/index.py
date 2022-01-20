import pygame
import os
pygame.init() 

width = 1200 
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) 
assets_path = os.path.join(current_path, 'assets')

invaders = []

class Alien:
	dx = 5
	def __init__(self, x, y, alienType):
		self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, alienType+'.png')), (35, 35))
		self.x = x
		self.y = y
		self.dead = False
	
	
	def update(self):
		if self.x > 1100 or self.x < 50:
			Alien.dx *= -1
			for i in invaders: 
				i.y += 25
				i.x += Alien.dx
				print(i.x)
				
		else:
			self.x += Alien.dx
		 
		if self.dead == False: screen.blit(self.imageLoaded, (self.x, self.y))
				
		return dx 
		


class Player: 	
	def __init__(self): 
		self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'ship.png')), (35, 35)) 
		self.x = width//2
		self.dx = 0
		self.bullet = []

def createInvaders(number):
	n = 0 
	x = 50 
	y = 50 
	for i in range(number):
		if n >= 15: # After 15 characters spawned, change rows
			y += 50
			x = 50
			n = 0 
		
		invaders.append(Alien(x, y, "InvaderA1"))
		x += 50
		n += 1

		
createInvaders(21) 
dx = 8

endProgram = False
while endProgram == False:
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT:
			endProgram = True

	screen.fill((0, 0, 0))		
	
	for i in invaders: i.update()
		

	pygame.display.update()
	clock.tick(30)
	
pygame.quit()
quit()

