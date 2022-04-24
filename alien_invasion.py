import sys
import pygame
from settings import Settings


class AlienInvasion:
    """class to control game resources and behaviour"""

    def __init__(self):
        """game inicialization and creation of resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion by splinter928")

    def run_game(self):
        """start of main game cycle"""
        while True:
            # tracking keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # filling the screen with background color (rendering)
            self.screen.fill(self.settings.bg_color)
            # displaying the last drawn screen
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
