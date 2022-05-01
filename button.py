import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """initializing button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # assigning button sizes and attributes
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (0, 0, 0)
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