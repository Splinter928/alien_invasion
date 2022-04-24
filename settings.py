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
