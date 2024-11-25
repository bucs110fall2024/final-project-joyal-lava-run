import pygame


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes enemy object
        args:
         - x: int - starting x coordinte
         - y: int - starting y coordintate
         - img: str - path to img file of enemy
        '''
        super().__init__()
        self.image = pygame.image.load("assets/enemies.png")   # Puts image on scree (dont reuse variable names)
        self.rect = self.image.get_rect()
        self.rect.center = [700, 300]          
        
    def moving(self):
        '''
        Moves back and forth along the platform
        args: None
        return: None
        '''
        pass
    
    def shoot(self):
        '''
        Shoots a bullet object at the player to try and kill them
        args: None
        return: bullet
        '''
        pass
    
    def turn(self):
        '''
        Turns automatically toward the player instead of facing one direction
        args: None
        return: None
        '''
        pass