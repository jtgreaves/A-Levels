import pygame
import os
import random
pygame.init() 

width = 1200 
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) 
assets_path = os.path.join(current_path, 'assets')

class Alien:
        dx = 5
        change = False #Whether they need to move down & change direction
        bullets = []
        
        def __init__(self, x, y, alienType):
                self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, alienType+'.png')), (35, 35))
                self.x = x
                self.y = y
                self.dead = False
        
        
        def update(self):
                if self.dead == False:
                        if (self.x + Alien.dx) >= 1100 or (self.x + Alien.dx) <= 50: Alien.change = True 
                        
                        self.x += Alien.dx
                        a = screen.blit(self.imageLoaded, (self.x, self.y))

                        for b in player.bullets: # Check whether they've been killed
                                if a.collidepoint(b.x, b.y):
                                        player.bullets.remove(b)
                                        self.dead = True

                        if self.y > 650: screen.fill((255,0,0)) # Check whether they've reached the player

                        chance = random.randint(0, 1000)
                        if chance == 0: Alien.bullets.append(Bullet(self.y, (self.x + 13), 1))

                                
                        

        def changeDirection():
                Alien.dx *= -1
                for i in invaders:
                        i.y += 25
                        i.x += Alien.dx
                Alien.change = False
                                
                


class Player:   
        def __init__(self): 
                self.imageLoaded = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'ship.png')), (35, 35)) 
                self.x = width//2
                self.bullets = []
                self.dx = 0
                self.lives = 3
                

        def update(self):
                for b in self.bullets: b.update()
                
                
                if player.x + self.dx > 55 and player.x + self.dx < 1100: self.x += self.dx
                p = screen.blit(player.imageLoaded, (self.x, 650))

                for b in Alien.bullets:
                        if p.collidepoint(b.x, b.y): screen.fill((255, 0, 0))

def createInvaders(number):
        n = 0 
        x = 50
        y = 50 
        for i in range(number):
                if n >= 15: # After 15 characters spawned, change rows
                        y += 50
                        x = 50
                        n = 0 
                
                invaders.append(Alien(x, y, "InvaderA1"))
                x += 50
                n += 1

class Bullet:
        playerBullet = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, 'bullet.png')), (10, 10))

        def __init__(self, y, x, direction, speed=10):
                self.y = y
                self.x = x
                self.speed = speed
                self.direction = direction #0 = UP; 1 = DOWN

        def update(self):
                if self.y > height or self.y < 0:
                        if self.direction == 1: Alien.bullets.remove(self)
                        else: player.bullets.remove(self)
                if self.direction == 0: self.y += -self.speed
                else: self.y += self.speed
                       
                screen.blit(Bullet.playerBullet, (self.x, self.y))

                

invaders = []
player = Player()
createInvaders(21)

endProgram = False
while endProgram == False:
        for e in pygame.event.get(): 
                if e.type == pygame.QUIT:
                        endProgram = True

                keys = pygame.key.get_pressed()
                if e.type == pygame.KEYDOWN: # Change direction if a new key is pressed 
                        if e.key == pygame.K_RIGHT: player.dx = 7
                        if e.key == pygame.K_LEFT: player.dx = -7

                        if e.key == pygame.K_SPACE: player.bullets.append(Bullet(650, (player.x + 13), 0))
                        
                if e.type == pygame.KEYUP: # Changes direction when a key is released; checks opposing direction's key
                        if e.key == pygame.K_RIGHT:
                                if keys[pygame.K_LEFT] == 1: player.dx = -7
                                else: player.dx = 0
                        elif e.key == pygame.K_LEFT:
                                if keys[pygame.K_RIGHT] == 1: player.dx = 7
                                else: player.dx = 0

                        

        screen.fill((0, 0, 0))
        
        for i in invaders: i.update()
        if Alien.change: Alien.changeDirection()
        for b in Alien.bullets: b.update()

        
        player.update()
        

        pygame.display.flip()
        clock.tick(30)
        
pygame.quit()
quit()

