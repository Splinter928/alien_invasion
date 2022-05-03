import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """initializing button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # assigning button sizes and attributes
        self.width, self.height = 200, 50
        self.button_color = self.settings.RED
        self.text_color = self.settings.BLACK
        self.font = pygame.font.SysFont(None, 48)

        # building a button rect object and alignment by screen center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """converts the msg to a rectangle and aligns the text to the center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """displaying an empty button and printing a message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class StartScreen:

    def __init__(self, ai_game):
        """initializing start screen attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.button = ai_game.play_button
        self.text_color_instr = self.settings.RED
        self.font_instr = pygame.font.SysFont(None, 24)

        self.instructions = {}
        self._prep_instructions()

    def _prep_instructions(self):
        text_instructions = ["'ENTER' or click the 'Play' - start/restart game",
                             "<-   -> - steer the ship",
                             "'SPACE' - fire",
                             "'ESC' - exit",
                             "'P' - pause/resume"]
        for i, text in enumerate(text_instructions):
            self.instr_image = self.font_instr.render(text, True, self.text_color_instr)
            self.instr_image_rect = self.instr_image.get_rect()
            self.instr_image_rect.center = self.button.rect.center
            self.instr_image_rect.top = 100 + self.button.rect.bottom + 30 * i
            self.instructions[self.instr_image] = self.instr_image_rect

    def draw_instructions(self):
        for img, rect in self.instructions.items():
            self.screen.blit(img, rect)
