import pygame

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/goku_shot.png")   # Puts image on scree (dont reuse variable names)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = [125, 390]
        self.speed = 3
        
    def update(self):
        self.rect.x += self.speed
          