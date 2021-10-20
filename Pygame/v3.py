from pygame import * 
init() 

width = 720 
height = 480 
screen = display.set_mode((width, height)) # tuple 

display.set_caption('Graphics') 
animationTimer = time.Clock() 

ball = Rect(100,200,40,40) 

x=150 
y=150 
dx = 2 # how fast/direction in x 
dy = 2 # how fast/direction in y 

px = 0
py = 0

endProgram = False 

# game loop
# check input 
# Update positions / game logic 
# draw frame 

while not endProgram: 
	for e in event.get(): 
		if e.type == QUIT: 
			endProgram = True 
		if e.type == KEYDOWN:
			if e.key == K_w:
				print("W")
				py = -2 
			elif e.key == K_a: 
				print("A")
				px = -2
			elif e.key == K_s: 
				print("S")
				py = 2
			elif e.key == K_d:
				print("D")
				px = 2
			elif e.key == K_ESCAPE: 
				endProgram = True
			else: 
				print("Other key pressed")
		elif e.type == KEYUP:
			if e.key == K_w:
				print("W")
				if py < 0: py = 0
			elif e.key == K_a: 
				print("A")
				if px < 0: px = 0
			elif e.key == K_s: 
				print("S")
				if py > 0: py = 0 
			elif e.key == K_d:
				print("D")
				if px > 0: px = 0
			elif e.key == K_ESCAPE: 
				endProgram = True

			
	# draw stuff 
	screen.fill((100,100,200))
	draw.ellipse(screen, (0,255,0), ball)
	ball.move_ip(px,py)
	animationTimer.tick(100)
	# update the screen! 
	display.update()
