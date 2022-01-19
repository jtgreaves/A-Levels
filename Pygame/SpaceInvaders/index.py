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
	def __init__(self, x, y, alienType):
		self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, alienType+'.png')), (35, 35))
		self.x = x
		self.y = y
		self.dead = False
			
	def draw(self):
		if self.dead == False: screen.blit(self.imageLoaded, (self.x, self.y))

def createInvaders(number):
	n = 0 
	x = 50 
	y = 50 
	for i in range(number):
		if n >= 15: # After 15 characters spawned, change rows
			y += 75
			x = 50
			n = 0 
		
		invaders.append(Alien(x, y, "InvaderA1"))
		x += 50
		n += 1

		
createInvaders(50) 
print(invaders)

dx = 10

endProgram = False
while endProgram == False:
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT:
			endProgram = True

	screen.fill((0, 0, 0))

	
	for i in invaders: 
		i.draw()
		
		if i.x > 1100 or i.x < 100: dx *= -1  
		i.x += dx 
		
	
	pygame.display.update()
	clock.tick(30)
	
pygame.quit()
quit()

