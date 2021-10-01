from pygame import * 
init() 

width = 900 
height = 500
screen = display.set_mode((width, height)) # tuple 

display.set_caption('Pong Game!')
animationTimer = time.Clock() 

playerHeight = 100

player1 = Rect(0, 200, 5, playerHeight)
player2 = Rect((width-5), 200, 5, playerHeight)

ball = Rect(width/2, height/2, 25, 25)

p1y = 0
p2y = 0

x=150 
y=150 
ballSpeed = 5

playerSpeed = 5
endProgram = False 

while not endProgram: 
	for e in event.get(): 
		if e.type == QUIT: 
			endProgram = True 
		if e.type == KEYDOWN:
			if e.key == K_w:
				print("W")
				p1y = -playerSpeed
			elif e.key == K_s: 
				print("S")
				p1y = playerSpeed
			elif e.key == K_UP: 
				print("UP")
				p2y = -playerSpeed
			elif e.key == K_DOWN:
				print("DOWN")
				p2y = playerSpeed
			elif e.key == K_ESCAPE: 
				endProgram = True
			else: 
				print("Other key pressed")
		elif e.type == KEYUP:
			if e.key == K_w:
				print("W")
				if p1y < 0: p1y = 0
			elif e.key == K_s: 
				print("S")
				if p1y > 0: p1y = 0
			elif e.key == K_UP: 
				print("UP")
				if p2y < 0: p2y = 0
			elif e.key == K_DOWN:
				print("DOWN")
				if p2y > 0: p2y = 0


			
	# draw stuff 
	screen.fill((100,100,200))
	
	
	if (player1.centery > playerHeight/2) and (p1y < 0):
		player1.move_ip(0,p1y)
	elif(player1.centery < height - playerHeight/2) and (p1y > 0):
		player1.move_ip(0,p1y)

	
	if (player2.centery > playerHeight/2) and (p2y < 0):
		player2.move_ip(0,p2y)
	elif(player2.centery < height - playerHeight/2) and (p2y > 0):
		player2.move_ip(0,p2y)

	draw.rect(screen, (0,255,0), player1) 
	draw.rect(screen, (0,255,0), player2) 

	ball.move_ip(1, 1)
	draw.ellipse(screen, (255,255,255), ball)

	

	animationTimer.tick(100)
	# update the screen! 
	display.update()
