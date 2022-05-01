class Settings:
    """class for storing game settings"""

    # colors (R, G, B)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self):
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)  # background color

        # ship parameters
        self.ship_speed = 1
        self.ship_limit = 3

        # bullets parameters
        self.bullet_speed = 1
        self.bullet_width = 1
        self.bullet_height = 50
        self.bullet_color = self.RED
        self.bullets_allowed = 5

        # aliens parameters
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 - move to the right, -1 - move to the left
