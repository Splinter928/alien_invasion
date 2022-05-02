class GameStats:
    """Collecting game statistic"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.read_high_score()

    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.ships_left = self.settings.ship_limit

    def read_high_score(self):
        try:
            with open('high_score.txt') as f:
                self.high_score = int(f.read())
        except:
            self.high_score = 0
