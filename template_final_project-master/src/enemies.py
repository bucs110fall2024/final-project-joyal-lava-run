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
        self.image = pygame.image.load("assets/enemies.png")   
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [800, 520]
        self.speed = 2          
        
    def moving(self):
        if 850 >= self.rect.x >= 700:
            self.rect.x -= self.speed
        else:
            self.speed *= -1
            self.rect.x -= self.speed 
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