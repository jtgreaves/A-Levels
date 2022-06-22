import pygame, random

pygame.init()
screenSize = [750, 750]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
pygame.display.set_caption("Blackjack - Joshua Greaves")

clock = pygame.time.Clock()


class AbstractScreen:
	def updateScreen(self): 
		pass 

	def drawScreen(self, screen):
		pass
	
	def handleInput(self, e):
		pass

	def nextScreen(self):
		return self
		
class GameScreen(AbstractScreen): 
	pass 

class Card(): 
	def __init__: 
		

currentScreen = GameScreen()

endProgram = False 
while endProgram == False: 
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			endProgram = True				
		currentScreen.handleInput(e)
	
	currentScreen.updateScreen()
	currentScreen.drawScreen(screen)
	currentScreen = currentScreen.nextScreen()
	
	pygame.display.flip()
	clock.tick(30) 

pygame.quit()
quit("Program ended")
