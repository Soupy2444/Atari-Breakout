import pygame, sys, random
from pygame.locals import *
import math
import pygame

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BACKGROUNDCOLOR = (0, 0, 0)

#colors
WHITE = (192, 192, 192)
GREEN = (0, 200, 0)
BLUE = (0, 0, 128)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

def Block(pygame.sprite.Sprite):
    
#block size
block_width = 20
block_height = 15

#row of blocks
for row in range(5):
    for column in range(0, blockcount):
        block = Block(blue, column * (block_width))
        blocks.add(block)
    top += block_height + 2
    
def paddle(color, width, height):
    super().paddle()
    
    #makes background transparent and sets x/y position
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
    
    #creates the rectangle
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()

#create the ball
def ball(pygame.sprite.Sprite):
    speed = 9.0
    #position of ball
    x = 0.0
    y = 175.0
    #Direction of ball ib degrees
    direction = 200
    width = 10
    height = 10
    
    #create the image of the ball
    self.image = pygame.Surface([self.width, self.height])
    
    self.image.fill(white)
    self.rect = self.image.get_rect()
    
def bounce(self, diff):
    #makes the ball bounce
    self.direction = (180 - self.direction) % 360
    self.direction -= diff
    
#updates where the ball is after a bounce
def update(self):
    direction_radians = math.radians(self.direction)
    
#changes the postiton of the ball depending on how fast and the direction its going
    self.x += self.speed * math.sin(direction_radians)
    self.y -= self.speed * math.cos(direction_radians)

#Makes it so it bounces off the top, left and right, but if it hits the bottom the games over
    if self.y <= 0:
        self.bounce(0)
        self.y = 1
    if self.x <= 0:
        self.direction = (360 - self.direction) % 360
        self.x = 1
    if self.x > self.screenwidth - self.width:
        self.direction = (360 - self.direction) % 360
        self.x = self.screenwidth - self.width - 1
    if self.y > 600:
        return True
    else:
        return False

#creating the bar at bottom
class Player(pygame.sprites.Sprites):
    
    def __init__(self):
        super().__init__()
        
        self.width = 70
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))
        
        #makes the bar follow the mouse
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
            
# makes the screen size
screen = pygame.display.set_mode([800, 600])

#makes a title for the game
pygame.display.set_caption('Breakout')

# looks to see if the ball hits the block and if it does the block disapears
    deadblocks = pygame.sprite.spritecollide(ball, block, True)

















pygame.quit()
    