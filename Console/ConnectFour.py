import pygame 
pygame.init()

width = 700
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
endProgram = False

def updateScreen(grid):
	row = 0 
	while row < len(grid): 
		column = 0 
		while column < len(grid[row]):
			x = (55 * column) + 25
			y = (55 * row) + 25
			if grid[row][column] == "R": colour = (255, 0, 0)
			elif grid[row][column] == "Y": colour = (200, 200, 50)
			elif grid[row][column] == "B": colour = (255, 255, 255)
			pygame.draw.circle(screen, colour, (x,y),25)
			column += 1
		row += 1 

	
	
grid = [["R", "", "", "", "", ""],["", "", "", "", "", ""],["", "", "", "", "", ""],["", "", "", "", "", ""],["", "", "", "", "", ""],["", "", "", "", "", ""],["", "", "", "", "", ""],["", "", "", "", "", ""]]
while endProgram == False:
	for e in pygame.event.get(): 
		if e.type == pygame.QUIT:
			endProgram = True

		
	screen.fill((50, 50, 50))
	
	updateScreen(grid) 

	
	pygame.display.update()
	clock.tick(30)


