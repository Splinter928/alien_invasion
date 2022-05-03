import pygame


class Sound:

    def __init__(self):
        self.music = pygame.mixer.music
        self.load_sounds()
        self.set_volumes()

    def load_sounds(self):
        self.sound_shot = pygame.mixer.Sound("sounds/blast.mp3")
        self.sound_prise = pygame.mixer.Sound("sounds/r2d2.mp3")
        self.music.load("sounds/star-wars-imperial-march.mp3")

    def set_volumes(self):
        self.music.set_volume(0.1)
        self.sound_shot.set_volume(0.2)
        self.sound_prise.set_volume(0.3)
