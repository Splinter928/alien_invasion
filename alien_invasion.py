import sys
from time import sleep
from math import floor

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """class for control game resources and behaviour"""

    def __init__(self):
        """game initialization and creation of resources"""
        pygame.init()
        self.settings = Settings()

        # window mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # full-screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion by splinter928")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # creating a Play-button
        self.play_button = Button(self, 'PLAY')

    def run_game(self):
        """main game cycle"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # tracking keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # launches a new game when the play button is
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.start_game()

    def start_game(self):
        # reset game statistics
        self.stats.reset_stats()
        self.stats.game_active = True

        # clearing alien and bullet lists
        self.aliens.empty()
        self.bullets.empty()

        # creating a new fleet and placing the ship in the center
        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif not self.stats.game_active and event.key == pygame.K_p:
            self.start_game()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # bullet creation and including it to the group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # refresh bullets position
        self.bullets.update()
        # delete bullets, which already out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # checking for bullets hitting aliens and destroy them if True
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # destroy existing bullets and create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            # processing aliens hitting ship
            self.stats.ships_left -= 1
            # clearing aliens and bullets lists
            self.aliens.empty()
            self.bullets.empty()
            # create new fleet and restore default ship position
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # checking aliens - ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # checking aliens - screen bottom collision
        self._check_aliens_bottom()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaliable_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = floor(avaliable_space_x // (alien_width * 1.5))
        ship_height = self.ship.rect.height
        avaliable_space_y = self.settings.screen_height - 2 * alien_height - ship_height
        number_rows = avaliable_space_y // (alien_height * 2)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 1.75 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        # reaction for the alien near edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # lowers the fleet and change direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        # filling the screen with background color (rendering)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # the play button is displayed if the game is not active
        if not self.stats.game_active:
            self.play_button.draw_button()

        # displaying the last drawn screen
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
