from pygame import *
import random 
import time as t
init() 

width = 900 
height = 500
screen = display.set_mode((width, height)) # tuple 

display.set_caption('Pong Game!')
animationTimer = time.Clock() 

playerHeight = 100

player1 = Rect(0, 200, 5, playerHeight)
player2 = Rect((width-5), 200, 5, playerHeight)

startTime = t.localtime() # Count up clock

ball = Rect(width/2, height/2, 25, 25)

p1y = 0
p2y = 0

x=150 
y=150

dx = -3
dy = 1
print(dx, dy)
ballSpeed = 10
x
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
	screen.fill((0,0,0))
	
	
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
	
	if ball.colliderect(player1): 
		ballPos = player1.center[1] - ball.center[1]
		if ballPos > 15:
			dx *= -1 
			dy = -1

		if ballPos < 15 and ballPos > -15:
			dx *= -1 
			dy *= -1
		
		if ballPos < -20:
			dx *= -1 
			dy = 1
	
	if ball.colliderect(player2): 
		ballPos = player2.center[1] - ball.center[1]
		if ballPos > 15:
			dx *= -1 
			dy = -1

		if ballPos < 15 and ballPos > -15:
			dx *= -1 
			dy *= -1
		
		if ballPos < -15:
			dx *= -1 
			dy = 1

	if ball.y < 0 or ball.y > height-20:
		dy *= -1
		
	#print(ball.x, ball.y)
	
	draw.ellipse(screen, (255,255,255), ball)
	ball.move_ip(dx, dy)
	
	animationTimer.tick(100)
	# update the screen! 
	display.update()
