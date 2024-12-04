import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/lava.png")
        self.image = pygame.transform.scale(self.image, (1000, 2000))
        self.rect = self.image.get_rect()
        self.rect.center = [500, 1750]
    
    def moving(self):
        self.rect.y -= 1.5