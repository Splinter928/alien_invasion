import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """class for printing game information"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = self.settings.RED
        self.font = pygame.font.SysFont(None, 32)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """converts the current score to an image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "score: {:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # print score in the top right part of the screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 5
        self.score_rect.top = 5

    def prep_high_score(self):
        """converts the high score to an image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "high score: {:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # print high score in the top center part of the screen
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = "level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # print level under the current score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 5
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

