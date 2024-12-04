import pygame
from src.shoot import Shoot

class Goku(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/goku.png")   # Puts image on scree (dont reuse variable names)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [125, 390]          
        self.shoot = Shoot() 
        
    def shooting(self):
        self.shoot.shot_out()
    