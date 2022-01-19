import pygame 
import random
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()


width = 1280 # 100 per X/O and then 25 spacing between
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) 
assets_path = os.path.join(current_path, 'assets')

genFont = pygame.font.SysFont('Calibri Light', 65)
presentAssets = ["present1.png", "present2.png" ,"present3.png","present4.png","present5.png","present6.png"]


backgroundMusic = os.path.join(assets_path, 'backgroundMusic.ogg')
pygame.mixer.music.load(backgroundMusic)
pygame.mixer.music.play()

class present: 
	def __init__(self, Y=None): 
		self.x = random.randint(50, width-50)
		if Y == None: self.y = -random.randint(0, 150)
		else: self.y = Y
		
		if random.randint(0, 20) < 5:
			if random.randint(0, 1) == 1:
				self.imageFile = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'coal.png')), (50, 50))
			else:
				self.imageFile = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'coal2.png')), (50, 50))
			self.bad = True
		else: 
			self.imageFile = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, str(presentAssets[random.randint(0, len(presentAssets)-1)]))), (50, 50))
			self.bad = False
		
	def generalOriginPresents(): 
		objects = []
		lastX = width

		while len(objects) < 5:
			y = -random.randint(0, 300)
			objects.append(present(y))

		return objects

#coal = pygame.image.load(os.path.join(assets_path, 'coal.png'))
snow = []

playerAsset = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "hands.png")), (75, 75))
playerX = 640

fallingItems = present.generalOriginPresents()
score = 0

for x in range(50):
	snow.append(pygame.Rect(random.randint(0,width), random.randint(0,height),3,3))

movingLeft = False
movingRight = False

endProgram = False
while endProgram == False:
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT: 
			endProgram = True
		elif e.type == pygame.KEYDOWN: 
			if e.key == pygame.K_LEFT:
				movingLeft = True
				movingRight = False
			elif e.key == pygame.K_RIGHT:
				movingLeft = False
				movingRight = True
		elif e.type == pygame.KEYUP:
			if e.key == pygame.K_LEFT:
				movingLeft = False
			elif e.key == pygame.K_RIGHT: 
				movingRight = False
	screen.fill((0, 0, 0))

	for flake in snow:
		flake.move_ip(random.randint(-2,2),random.randint(1,4))
		if flake.y > height:
			flake.x = random.randint(0,width)
			flake.y = -3
		pygame.draw.rect(screen, (255,255,255), flake)

	if movingRight: playerX += 15
	elif movingLeft: playerX -= 15
	player = screen.blit(playerAsset, (playerX, height-75))	

	for obj in fallingItems: 
		screen.blit(obj.imageFile, (obj.x, obj.y))
		obj.y += 10
		
		if player.collidepoint(obj.x, obj.y):
			if obj.bad == False: score += 1
			else: score -= 1
			obj.x = random.randint(50, width-50)
			obj.y = -random.randint(0, 150)
		
		if obj.y > height: 
			obj.x = random.randint(50, width-50)
			obj.y = -random.randint(0, 150)
		
		scoreText = genFont.render(str(score), False, (255, 255, 255))
		screen.blit(scoreText, scoreText.get_rect(center=(width//2, 50)))
	
	pygame.display.update()
	clock.tick(30)
	
pygame.quit()
quit()
