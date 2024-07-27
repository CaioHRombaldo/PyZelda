import pygame

class Level:
    def __init__(self):

        # sprite group setup
        self.visible_sprite = pygame.sprite.Group()
        self.obstacles_sprite = pygame.sprite.Group()

    def run(self):
        # update and draw the game
        pass