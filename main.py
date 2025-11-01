import pygame
from pygame.locals import *
from sys import exit

# https://coderslegacy.com/python/python-pygame-tutorial/
# Initialize Pygame; must have line

pygame.init()

# Top left (0,0), bottom right (300, 300)
DISPLAYSURF = pygame.display.set_mode((300, 300))

while True:
    # loop over every event in the list, exec code on selected actions
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
