import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # class representing a single alien

    def __init__(self, ai_game):
        """Initialization of alien and it's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/tie-fighter.png')
        self.rect = self.image.get_rect()

        # Every new alien starts near left top part of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height // 2

        self.x = float(self.rect.x)

    def check_edges(self):
        # check if alien near the screen edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # move alien to the right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
