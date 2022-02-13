import pygame
import os
import random
import math
import json
pygame.init()

width = 1200
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
levels_path = os.path.join(current_path, 'levels')
heartImage =  pygame.image.load(os.path.join(assets_path, 'heart.png'))

class Alien:
	dx = 5
	change = False #Whether they need to move down & change direction
	bullets = []

	def __init__(self, x, y, alienType, dead=False):
		self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, alienType+'.png')), (35, 35))
		self.x = x
		self.y = y
		self.dead = dead


	def update(self, player):
		if self.dead == False:
			if (self.x + Alien.dx) >= 1100 or (self.x + Alien.dx) <= 50: Alien.change = True

			self.x += Alien.dx
			a = screen.blit(self.imageLoaded, (self.x, self.y))

			
			if a.collidepoint(player.bullet.x, player.bullet.y):
				player.bullet = pygame.Rect(0,0,0,0)
				self.dead = True

			if self.y > 650: 
				player.kill(player.lives)

			
			chanceInt = 1000 - 50*(3-len(Alien.bullets))
			if chanceInt <= -0: chanceInt = 1000 
			
			chance = random.randint(0, chanceInt)
			if chance == 0: Alien.bullets.append(Bullet(self.y, (self.x + 13), 1))

	def changeDirection(invaders):
		Alien.dx *= -1
		for i in invaders:
			i.y += 25
			i.x += Alien.dx
		Alien.change = False
	
	def create(aliens): 
		total = 0
		x = 50 
		y = 75
		
		invaders = []
		for alien in aliens:
			if total >= 15: 
				y += 50 
				x = 50 
				total = 0 
			
			if alien == 1: invaders.append(Alien(x, y, "InvaderA1"))
			elif alien == 2: invaders.append(Alien(x, y, "InvaderA2"))
			elif alien == 3: invaders.append(Alien(x, y, "InvaderB1"))
			elif alien == 4: invaders.append(Alien(x, y, "InvaderB2"))
			else: invaders.append(Alien(0, 0, "InvaderA1", True)) # If the alien is dead or an invalid state 
			
			x+= 50 
			total += 1
		
		return invaders

class Player:
	def __init__(self, lives):
		self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'ship.png')), (35, 35))
		self.x = width//2
		self.bullet = pygame.Rect(0, 0, 0, 0)
		self.dx = 0
		self.lives = lives


	def update(self):
		if self.bullet != pygame.Rect(0, 0, 0, 0): self.bullet.update(self)
		
		if self.x + self.dx > 55 and self.x + self.dx < 1100: self.x += self.dx
		p = screen.blit(self.imageLoaded, (self.x, 650))

		for b in Alien.bullets:
			if p.collidepoint(b.x, b.y): 
				self.kill()
				Alien.bullets.remove(b)
		
		if self.lives <= 0:
			endProgram = True
			self.lives
		
	def kill(self, amount=1): 
		screen.fill((255, 0, 0))
		self.lives -= amount

class Bullet:
	playerBullet = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'bullet.png')), (10, 10))

	def __init__(self, y, x, direction, speed=10):
		self.y = y
		self.x = x
		self.speed = speed
		self.direction = direction #0 = UP; 1 = DOWN

	def update(self, player):
		if self.y > height or self.y < 0:
			if self.direction == 1: Alien.bullets.remove(self)
			else: player.bullet = pygame.Rect(0,0,0,0)
		if self.direction == 0: self.y += -self.speed
		else: self.y += self.speed
		
		screen.blit(Bullet.playerBullet, (self.x, self.y))

class Barricade: 
	def __init__(self, start, length, h=25):
		self.startPoint = start
		self.length = length
		self.lines = [] #Each value is the endpoint of another line 
		
		bias = h /(length//2)
		backwardsCount = 0
		for l in range(length):
			if l < length//2: lineHeight = math.floor(h + bias*l)
			else: 
				lineHeight = math.floor(h + bias*(l-backwardsCount))
				backwardsCount += 2
			
			self.lines.append([height-150, lineHeight])# [Bottom, height]
		
	
	def create(number):
		barricades = [] 
		for n in range(number): 
			barricades.append(Barricade(n*50+55, 25)) #Start point & length
		return barricades
	
	def update(self, player):
		bias = 0
		line = 0 
		while line < len(self.lines):
			if self.lines[line][1] > 0: 
				ba = pygame.draw.line(screen, (255, 255, 255), (self.startPoint+bias, self.lines[line][0]), (self.startPoint+bias, self.lines[line][0]-self.lines[line][1]), 7)
				
				for b in Alien.bullets:
					if ba.collidepoint(b.x, b.y): 
						self.lines[line][1] -= 10
						Alien.bullets.remove(b)
				
				if ba.collidepoint(player.bullet.x+10, player.bullet.y+5):
					self.lines[line][0] -= 10
					self.lines[line][1] -= 10
					player.bullet = pygame.Rect(0,0,0,0)
				
			bias += 7
			line += 1  

class AbstractScreen:
	def drawScreen(self, screen):
		pass
	
	def handleInput(self, e):
		pass

	def nextScreen(self):
		return self
		
class MainScreen(AbstractScreen):
	def __init__(self):
		levelData = self.loadLevel(3)
		
		print(levelData)
		self.name = levelData["levelName"]
		self.invaders = Alien.create(levelData["invaders"])
		self.barricades = Barricade.create(levelData["barricades"]) # Temporarily an int 
		self.player = Player(levelData["lives"])
	
	def drawScreen(self, screen):
		screen.fill((0, 0, 0))
		for life in range(self.player.lives):
			screen.blit(heartImage, (10+(life*40), 10))
			

		for i in self.invaders: i.update(self.player)
		if Alien.change: Alien.changeDirection(self.invaders)
		for b in Alien.bullets: b.update(self.player)
		for b in self.barricades: b.update(self.player)
	
		self.player.update()
	
	def handleInput(self, e):
		keys = pygame.key.get_pressed()
		if e.type == pygame.KEYDOWN: # Change direction if a new key is pressed
			if e.key == pygame.K_RIGHT: self.player.dx = 7
			if e.key == pygame.K_LEFT: self.player.dx = -7

			if e.key == pygame.K_SPACE and self.player.bullet == pygame.Rect(0, 0, 0, 0): 
				self.player.bullet = Bullet(650, (self.player.x + 13), 0)
				self.frameCount = 20

		if e.type == pygame.KEYUP: # Changes direction when a key is released; checks opposing direction's key
			if e.key == pygame.K_RIGHT:
				if keys[pygame.K_LEFT] == 1: self.player.dx = -7
				else: self.player.dx = 0
			elif e.key == pygame.K_LEFT:
				if keys[pygame.K_RIGHT] == 1: self.player.dx = 7
				else: self.player.dx = 0

	def nextScreen(self):
		if self.player.lives <= 0:
			return GameOverScreen()
		return self
	
	def loadLevel(self, level): 
		jsonFile = open(os.path.join(levels_path, str(level) + ".json"))
		levelData = json.load(jsonFile)
		jsonFile.close()
		
		return levelData 

class GameOverScreen(AbstractScreen):
	def __init__(self): 
		self.replay = False
		
	def drawScreen(self, screen):
		screen.fill((0, 0, 0))
		titleFont = pygame.font.SysFont('Courier New', 65)
		title = titleFont.render("Game Over!", True, (255, 0, 0))
		screen.blit(title, title.get_rect(center=(width//2, 50))) 
		
	def nextScreen(self):
		if self.replay == True: return MainScreen()
		
		return self

endProgram = False
currentScreen = MainScreen()

while endProgram == False:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			endProgram = True
		currentScreen.handleInput(e)
	
	currentScreen.drawScreen(screen)
	currentScreen = currentScreen.nextScreen()
	
	pygame.display.flip()
	clock.tick(30)

pygame.quit()
quit()

