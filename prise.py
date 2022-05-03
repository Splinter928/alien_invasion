import pygame
from pygame.sprite import Sprite


class Prise(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/x-wing-50.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.y = float(self.rect.y)

    def update(self):
        # update prise position
        self.y += self.settings.prise_speed
        self.rect.y = self.y

