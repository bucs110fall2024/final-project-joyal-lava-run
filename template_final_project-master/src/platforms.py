import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/platform.png")   
        self.image = pygame.transform.scale(self.image, (200, 25))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]