import pygame


class Ship:
    def __init__(self, ai_game):
        """ Initialization of starship and it's starting position """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/lada.bmp')
        self.rect = self.image.get_rect()

        # Every new starship starts near bottom part of screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw starship in current position"""
        self.screen.blit(self.image, self.rect)
