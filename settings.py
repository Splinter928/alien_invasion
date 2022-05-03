class Settings:
    """class for storing game settings"""

    # colors (R, G, B)
    BLACK = (0, 0, 0)
    GRAY = (30, 30, 30)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self):
        """initializes static game settings"""
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = self.GRAY  # background color

        # ship parameters
        self.ship_start_limit = 2
        self.ship_max_limit = 5

        # bullets parameters
        self.bullet_width = 1
        self.bullet_height = 50
        self.bullet_color = self.RED
        self.bullets_allowed = 5

        # aliens parameters
        self.fleet_drop_speed = 10

        # prises parameters
        self.prise_chance = 5
        self.prise_allowed = 1

        # rate of acceleration of the game
        self.speedup_scale = 1.2
        self.ship_speedup_scale = 1.05
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initializes dynamic game settings"""
        self.ship_speed = 1
        self.bullet_speed = 1
        self.prise_speed = 0.75
        self.alien_speed = 0.2
        self.alien_points = 100

        self.fleet_direction = 1  # 1 - move to the right, -1 - move to the left

    def increase_speed(self):
        """increases speed settings"""
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.ship_speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
