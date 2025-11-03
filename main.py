from sys import exit
import pygame
from pygame.locals import *
import utils
from player import Player
from enemy import Enemy

# https://coderslegacy.com/python/python-pygame-tutorial/


# Initialize Pygame; must have line
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 20)

# Top left (0,0) is the origin
DISPLAYSURF = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))
DISPLAYSURF.fill(utils.WHITE)
pygame.display.set_caption("Pygame Boilerplate")


P1 = Player()
E1 = Enemy()
 
while running:     
    for event in pygame.event.get():              
        if event.type == pygame.QUIT:
            running = False
    P1.update()
    E1.move()
     
    DISPLAYSURF.fill(utils.WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    text = font.render(f"Score: {utils.score}", True, utils.BLACK)
    DISPLAYSURF.blit(text, (20, 20))     

    pygame.display.update()
    FramePerSec.tick(FPS)


pygame.quit()
exit()
