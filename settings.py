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
        self.bg_color = (200, 255, 230)  # background color

        # ship parameters
        self.ship_speed = 1.5

        # bullets parameters
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # aliens parameters
        self.alien_speed = 0.25
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 - move to the right, -1 - move to the left
