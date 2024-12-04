import pygame

class Helicopter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/helicopter.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = [900, 100]