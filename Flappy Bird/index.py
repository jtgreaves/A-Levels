from pygame import * 

init()
width = 1200
height = 700
screen = display.set_mode((width, height))

gameOver = False 

class Pipe(): 
	def __init__(self): 
		self.x = randint(40, 1200)
		self.y = randint(40, 700)
		self.dx = randint(-4, 4)
		self.dy = randint(-4, 4)
		if self.dx and self.dy == 0: dx = 1
		self.radius = randint(5, 50)
		self.colour = (250, 0, 0)
		
	def outputData(self):
		print(self.x, self.y, self.dx, self.dy, self.radius)
		
	def draw(self, screen):
		print(self.x, self.y, self.dx, self.dy, self.radius, self.colour)
		draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
		
while gameOver == False:
	for e in event.get():
		if e.type == QUIT: 
			gameOver = True
		if e.type == KEYDOWN:
			if e.key == K_ESC:
				gameOver = False
			elif e.key == K_SPACE:
				print("SPACE")
				
	screen.fill((255,255,255))
	myBall.draw(screen)
	display.flip()
	
	time.delay(1)
