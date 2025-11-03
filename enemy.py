"""A class to represent an enemy in a game."""
from random import randint
import pygame
import utils

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/enemy.png")
        self.rect = self.image.get_rect() # Get the rectangular area of the image
        self.rect.center = (randint(40, utils.SCREEN_WIDTH - 40), 0) # Start at a random position at the top

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > utils.SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (randint(30, utils.SCREEN_WIDTH - 30), 0)
            utils.score += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

            