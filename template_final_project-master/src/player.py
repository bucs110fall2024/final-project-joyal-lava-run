import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Initializes player object
        args:
         - x: int - starting x coordinte
         - y: int - starting y coordintate
         - img: str - path to img file of player
        '''
        super().__init__()
        self.image = pygame.image.load("assets/water_girl.png")   # Puts image on screen (dont reuse variable names)
        self.rect = self.image.get_rect()
        self.rect.center = [100, 400]          # Centers it at (100, 600)
        
    def move_right(self):
        '''
        Moves right when right arrow key is pressed until let go
        args: None
        return: None
        '''
        self.rect.x += 10
    
    def move_left(self):
        self.rect.x -= 10
        '''
        Moves left when left arrow key is pressed until let go
        args: None
        return: None
        '''
    
    def jumping(self):
        self.rect.y -= 10
        '''
        Moves up 1 when space or up arrow key is pressed
        args: None
        return: None
        '''
    
    def not_jumping(self):
        self.rect.y += 10
    
    def block(self):        # Hypothetical
        '''
        Blocks attack when shift key is presed  
        args: None
        return: None
        '''
        pass