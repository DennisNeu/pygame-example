"""A class to represent the player"""

import pygame
from pygame.locals import *
import utils

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/player.png")
        self.rect = self.image.get_rect()  # Get the rectangular area of the image
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
                
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if self.rect.right < utils.SCREEN_WIDTH:        
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)