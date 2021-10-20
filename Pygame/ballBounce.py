from pygame import * 
init() 

width = 720 
height = 480 
screen = display.set_mode((width, height)) # tuple 

display.set_caption('Graphics') 
animationTimer = time.Clock() 

x=150 
y=150 
dx = 5 # how fast/direction in x 
dy = 1 # how fast/direction in y 

endProgram = False 

# game loop
# check input 
# Update positions / game logic 
# draw frame 

while not endProgram: 
  # Check input 
  for e in event.get(): 
    if e.type == QUIT: 
      endProgram = True 
      
  # update position
  x += dx 
  y += dy 
  
  # border check 
  if y<0 or y>height - 90 : 
    dy *= -1 
  if x<0 or x>width - 40: 
    dx *= -1 
  
  # draw stuff 
  screen.fill((100, 203, 255)) 
  # circle 

  draw.ellipse(screen, (255,255,255), (x, y, 40, 40))
  draw.ellipse(screen, (0,0,0), (x, y, 40, 40), 10)
  draw.rect(screen, (0, 255, 0), (0, height-50, width, 50))
  # limit to 30 frames per second 
  animationTimer.tick(100) 
  # update the screen! 
  display.update()
