import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class for control bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # bullet creation in position (0, 0) and moving it to the right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
        # bullet start x-coord correction because of shadow on the right side of ship model
        self.rect.x -= 4

    def update(self):
        # update bullet position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # fill draw rectangle with it color
        pygame.draw.rect(self.screen, self.color, self.rect)
